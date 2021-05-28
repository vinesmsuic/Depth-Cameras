import darknet
import ctypes
import math
import random
import os
from cv2 import cv2
import numpy as np
import statistics

#realsesnse cam related
from pyrealsense2 import pyrealsense2 as rs
import time



#File path for yolo cone detection
configPath = "./cfg/yolov4-tiny_conesdcm.cfg"
weightPath = "./backupdcmtiny10/yolov4-tiny_conesdcm_best.weights"
metaPath = "./data/conesdcmtiny.data"
netMain, ClassNameMain, _ = darknet.load_network(configPath, metaPath, weightPath)

# Function for getting depth data
def getDepth_dcm(detections, depthimg, img, colors):
    for label, confidence, bbox in detections:
        x, y, w, h = bbox
        x = round(x)
        y = round(y)
        print(f"For dected {label} with confidence {confidence}, Depth at x={x}, y={y} is {depthimg[y][x]}")
        #print("depth image of the boundary box is :")

        #get depth median in the detection bbox
        depth_bbox = depthimg[y-round(h/2):y+round(h/2),x-round(w/2):x+round(w/2)]
        arr = np.array(depth_bbox)
        depth_median = np.median(arr)
        #cv2.putText(img,f'{depthimg[y][x]/10}cm', (x+round(w/2),y+round(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[label], 1)
        cv2.putText(img,f'{depth_median/10}cm', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[label], 1)
        print(f"The distance of the cone is {depth_median/10}cm")
        #dot in bbox center
        cv2.circle(img, (x,y), radius=1, color=colors[label], thickness=-1)


#Function for realsense camera init

def realsense_init(device_id = '036522072893'):
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_device(device_id)
    config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)  # depth
    config.enable_stream(rs.stream.color, 424, 240, rs.format.bgr8, 30) # rgb
    config.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, 63) # acceleration
    config.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)  # gyroscope
    profile = pipeline.start(config)
    depth_sensor = profile.get_device().first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()
    print("Depth Scale is: " , depth_scale)
    align_to = rs.stream.color
    align = rs.align(align_to)
    colors = darknet.class_colors(ClassNameMain)
    return pipeline, align, colors


pipeline, align, colors = realsense_init()
try:
    frame_count = 0
    start_time = time.time()
    while True:

        # Wait for a synced pair of depth and color frames
        frames = pipeline.wait_for_frames()
        frame_time = time.time() - start_time
        frame_count += 1
        
        # get imu frames
        accel_frame = frames.first_or_default(rs.stream.accel, rs.format.motion_xyz32f)
        gyro_frame = frames.first_or_default(rs.stream.gyro, rs.format.motion_xyz32f)

        # Align the depth frame to color frame
        aligned_frames = align.process(frames) 
        depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.065), cv2.COLORMAP_JET)
        
        #detection with YOLO
        #rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Create an image for each detect
        darknet_image = darknet.make_image(color_image.shape[1], color_image.shape[0], 3)
        rgb_dcm = cv2.cvtColor(depth_colormap, cv2.COLOR_BGR2RGB)
        darknet.copy_image_from_bytes(darknet_image, rgb_dcm.tobytes())

        detections = darknet.detect_image(netMain, ClassNameMain, darknet_image, thresh=0.25)
        darknet.print_detections(detections, coordinates=True)

        imagedetected_dcm = darknet.draw_boxes(detections, depth_colormap, colors)
        getDepth_dcm(detections, depth_image, imagedetected_dcm, colors)
        imagedetected_color = darknet.draw_boxes(detections, color_image, colors)
        getDepth_dcm(detections, depth_image, color_image, colors)
        
        
        # Stack both images horizontally
        images = None
        images = np.hstack((color_image, depth_colormap))
        #images = depth_colormap

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        if images is not None:
            cv2.imshow('RealSense', images)
        #print(depth_image.shape)
        #print(color_image.shape)

        #print("accel at frame {} at time {}: {}".format(str(frame_count), str(frame_time), str(accel_frame.as_motion_frame().get_motion_data())))
        #print("gyro  at frame {} at time {}: {}".format(str(frame_count), str(frame_time), str(gyro_frame.as_motion_frame().get_motion_data())))

        # Press esc or 'q' to close the image window
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
        

finally:
    # Stop streaming
    pipeline.stop()

