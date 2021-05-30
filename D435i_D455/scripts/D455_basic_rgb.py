#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 #3.2.0

def callback(data):

    #use CvBridge to convert between ROS and OpenCV images
    br = CvBridge()

    #convert ROS image message to OpenCV image (BGRA)
    current_frame = br.imgmsg_to_cv2(data)

    bgr_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGRA2BGR)

    #convert to RGB for processing
    rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGRA2RGB)

    # Output debugging information to the terminal
    log = rgb_frame
    rospy.loginfo(log)

    cv2.imshow("intel camera", rgb_frame)

    cv2.waitKey(1)

def receive_message():

    # Tells rospy the name of the node.
    # Anonymous = True makes sure the node has a unique name. Random
    # numbers are added to the end of the name. 
    rospy.init_node('intel_camera_rgb', anonymous=True)

    # Node is subscribing to the rgb/image_raw topic
    rospy.Subscriber('camera/color/image_raw', Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    receive_message()
