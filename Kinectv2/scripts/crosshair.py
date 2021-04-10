#!/usr/bin/env python

import rospy
import message_filters # To Achieve Multiple subscriber
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 #3.2.0
import imutils

#This one is for KinectV2.

class Kinect_Node(object):
    def __init__(self):

        #use CvBridge to convert between ROS and OpenCV images
        self.br = CvBridge()

        # Node is subscribing to the /kinect2/sd/image_color_rect topic
        self.rgb_sub = message_filters.Subscriber('/kinect2/sd/image_color_rect', Image)

        # Node is subscribing to the /kinect2/sd/image_depth_rect
        self.depth_sub = message_filters.Subscriber('/kinect2/sd/image_depth_rect', Image)


    def callback(self, ros_rgb, ros_depth):

        timer = cv2.getTickCount()
        
        #convert ROS image message to OpenCV image 
        depth_frame = self.br.imgmsg_to_cv2(ros_depth, desired_encoding="32FC1")
        rgb_frame = self.br.imgmsg_to_cv2(ros_rgb, "bgr8")

        #resize image
        depth_frame = imutils.resize(depth_frame, width=600)
        rgb_frame = imutils.resize(rgb_frame, width=600)

        #get distances
        f_distance = get_distance(depth_frame)
        
        depth_frame = cv2.cvtColor(depth_frame, cv2.COLOR_GRAY2BGR)

        fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
        #rospy.loginfo("The fps is: %s", fps)

        

        draw_crosshair(rgb_frame, crosshair_color=(255,0,0))
        draw_crosshair(depth_frame, crosshair_color=(0,0,255))

        
        cv2.putText(rgb_frame, "cm:" + str(f_distance), (15,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA, False)

        cv2.putText(depth_frame, "fps:" + str(fps), (depth_frame.shape[1]-150,depth_frame.shape[0]-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA, False)

        #If we want to stablize, don't use imshow. Use a publisher to send the data out and use rqt_gui to see the frame.
        cv2.imshow("depth camera", depth_frame)
        cv2.imshow("rgb camera", rgb_frame)
        
        cv2.waitKey(1)


def get_distance(frame):
    img_height = frame.shape[0]
    img_width = frame.shape[1]
    x_center = img_width/2
    y_center = img_height/2
    #rospy.loginfo("The center pixel value is: %s", frame[y_center][x_center])
    
    distance = float(frame[y_center][x_center])/10
    distance_arr = frame[y_center-10:y_center+11,x_center-10:x_center+11]
    distance_arr = distance_arr.flatten()
    median = np.median(distance_arr)
    rospy.loginfo("The median distance is: %s cm", median)
    rospy.loginfo("The distance of center pixel is: %s cm", distance)

    return distance

def draw_crosshair(frame, crosshair_size=30, crosshair_color=(255,0,0), stroke=1):
    img_height = frame.shape[0]
    img_width = frame.shape[1]
    x_center = img_width/2
    y_center = img_height/2
    cv2.line(frame, (x_center-crosshair_size,y_center-crosshair_size), (x_center+crosshair_size,y_center+crosshair_size), crosshair_color, stroke)
    cv2.line(frame, (x_center+crosshair_size,y_center-crosshair_size), (x_center-crosshair_size,y_center+crosshair_size), crosshair_color, stroke)
    cv2.rectangle(frame, (x_center-crosshair_size,y_center-crosshair_size), (x_center+crosshair_size,y_center+crosshair_size), (255,0,0), 1)


def main():

    my_node = Kinect_Node()
    # Tells rospy the name of the node.
    # Anonymous = True makes sure the node has a unique name. Random
    # numbers are added to the end of the name. 
    rospy.init_node("Kinect_Distance_Node", anonymous=True)

    ts = message_filters.ApproximateTimeSynchronizer([my_node.rgb_sub, my_node.depth_sub], 10, 0.1)
    ts.registerCallback(my_node.callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    

if __name__ == '__main__':
    main()
