import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from std_msgs.msg import Float32MultiArray
from cv_bridge import CvBridge, CvBridgeError
import sys
import os
import numpy as np
import pyrealsense2 as rs2
import message_filters
if (not hasattr(rs2, 'intrinsics')):
    import pyrealsense2.pyrealsense2 as rs2
    
import darknet
import darknet_images
import ctypes
import math
import random
import os
import cv2
import numpy as np
import math
import multiprocessing as mp
import gc
#realsesnse cam related
import pyrealsense2 as rs
import time


class ROS_ConeDetector:
    def __init__(self,color_image_topic, depth_image_topic, depth_info_topic):
        #network init
        configPath = "./Detection_weights/yolov4-tiny_conesdcm.cfg"
        weightPath = "./Detection_weights/yolov4-tiny_conesdcm_best.weights"
        metaPath = "./Detection_weights/conesdcm.data"

        self.netMain, self.ClassNameMain, _ = darknet.load_network(configPath, metaPath, weightPath)
        self.colors = darknet.class_colors(self.ClassNameMain)

        self.frame_count = 0
        self.start_time = time.time()
        self.coord_pool = []
        #self.bridge = CvBridge()
        self.color_image_sub = message_filters.Subscriber(color_image_topic, Image)
        self.depth_image_sub = message_filters.Subscriber(depth_image_topic, Image)
        ts = message_filters.TimeSynchronizer([self.color_image_sub, self.depth_image_sub], 10)
        ts.registerCallback(self.detectionCallback)

        
        self.sub_info = rospy.Subscriber(depth_info_topic, CameraInfo, self.imageDepthInfoCallback)

        self.intrinsics = None
        self.pix = None
        self.pix_grade = None

    def detectionCallback(self, color_img, depth_img):
        print("Entered detection call back")
        frame_time = time.time() - self.start_time
        self.frame_count += 1

        # Convert images to numpy arrays
        depth_cv_image = np.frombuffer(depth_img.data, dtype=np.uint16).reshape(depth_img.height, depth_img.width, -1)
        depth_image = np.asanyarray(depth_cv_image)
        color_cv_image = np.frombuffer(color_img.data, dtype=np.uint8).reshape(color_img.height, color_img.width, -1)
        im_BGR = cv2.cvtColor(color_cv_image, cv2.COLOR_RGB2BGR)
        color_image = np.asanyarray(im_BGR)

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.065), cv2.COLORMAP_JET)
        
        #detection with YOLO
        detections = self.yolo_cone_detect(depth_colormap)
        imagedetected_dcm = darknet.draw_boxes(detections, depth_colormap, self.colors)

        self.cone_localization(detections, depth_image, color_image, self.colors, self.intrinsics)

        color_image = darknet.draw_boxes(detections, color_image, self.colors)
        
        # Stack both images horizontally
        images = np.hstack((color_image, imagedetected_dcm))

        fps = 1 / frame_time
        cv2.putText(images,"FPS: {}".format(fps), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
        self.start_time = time.time()
        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        if images is not None:
            cv2.imshow('RealSense', images)
        if self.coord_pool:
            self.coord_pool = []
        cv2.waitKey(1)

    #get camera intrinsics
    def imageDepthInfoCallback(self, cameraInfo):
        print("entered intrin callback")
        try:
            if self.intrinsics:
                return
            self.intrinsics = rs2.intrinsics()
            self.intrinsics.width = cameraInfo.width
            self.intrinsics.height = cameraInfo.height
            self.intrinsics.ppx = cameraInfo.K[2]
            self.intrinsics.ppy = cameraInfo.K[5]
            self.intrinsics.fx = cameraInfo.K[0]
            self.intrinsics.fy = cameraInfo.K[4]
            if cameraInfo.distortion_model == 'plumb_bob':
                self.intrinsics.model = rs2.distortion.brown_conrady
            elif cameraInfo.distortion_model == 'equidistant':
                self.intrinsics.model = rs2.distortion.kannala_brandt4
            self.intrinsics.coeffs = [i for i in cameraInfo.D]
        except CvBridgeError as e:
            print(e)
            return

    # Function for getting depth data
    def get_real_world_ccordinates(self, depth_intrin, color_image, depth_image, x, y, detection):
        # Intrinsics & Extrinsics
        depth_intrin = depth_intrin
        depth = depth_image[y][x]
        #2d to 3d coord
        coordinates = rs.rs2_deproject_pixel_to_point(depth_intrin, [x,y], depth)

        distance = math.sqrt(((coordinates[0])**2) + ((coordinates[1])**2) + ((coordinates[2])**2))
        print("Distance from camera to pixel:", distance)
        print(f"coordinates are {coordinates[0]} ,{coordinates[1]}, {coordinates[2]}")

        return coordinates

    def cone_localization(self,detections, depth_image, color_image, colors, depth_intrin):
        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_image)
        for i in range(len(detections)):
            label, confidence, bbox = detections[i]
            xmin = int(round(bbox[0] - (bbox[2] / 2)))
            xmax = int(round(bbox[0] + (bbox[2] / 2)))
            ymin = int(round(bbox[1] - (bbox[3] / 2)))
            ymax = int(round(bbox[1] + (bbox[3] / 2)))
            filtered_depth_img = cv2.GaussianBlur(depth_image, (3,3), 2, None, 2, cv2.BORDER_REPLICATE)
            depth_bbox = filtered_depth_img[ymin:ymax,xmin:xmax]

            arr = np.array(depth_bbox)
            depth_median = np.median(arr)

            coordinates = self.get_real_world_ccordinates(self.intrinsics, color_image, filtered_depth_img , bbox[2], bbox[3], detections[i]) 

            cv2.putText(color_image,f'{coordinates[0]}', (bbox[2], bbox[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[label], 1)
            cv2.putText(color_image,f'{coordinates[2]}', (bbox[2], bbox[3]+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[label], 1)
            
            #print(f"The distance of the cone is {coordinates[2]*100}cm")
            cv2.circle(color_image, (bbox[2], bbox[3]), radius=2, color=colors[label], thickness=-1)
            #cv2.imshow("color_image", color_image)
        return color_image


    def yolo_cone_detect(self, depth_colormap):
        #detection with YOLO
        #rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #Create an image for detecttion
        darknet_image = darknet.make_image(depth_colormap.shape[1], depth_colormap.shape[0], 3)
        rgb_dcm = cv2.cvtColor(depth_colormap, cv2.COLOR_BGR2RGB)
        darknet.copy_image_from_bytes(darknet_image, rgb_dcm.tobytes())
        detections = darknet.detect_image(self.netMain, self.ClassNameMain, darknet_image, thresh=0.55)
        #free image after detection
        darknet.free_image(darknet_image)
        darknet.print_detections(detections, coordinates=True)

        return detections





def main():
    depth_image_topic = '/camera/aligned_depth_to_color/image_raw'
    depth_info_topic = '/camera/aligned_depth_to_color/camera_info'
    color_image_topic = '/camera/color/image_raw'
    print ('')
    print ('ROS_DNdetection.py')
    print ('--------------------')
    
    listener = ROS_ConeDetector(color_image_topic, depth_image_topic, depth_info_topic)
    rospy.spin()

if __name__ == '__main__':
    node_name = os.path.basename(sys.argv[0]).split('.')[0]
    rospy.init_node(node_name)
    main()