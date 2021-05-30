#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 #3.2.0
import imutils

def showColoredMask(frame):
    
    #Purple
    colorLower = np.array([160,135,25])
    colorUpper = np.array([179,255,255])
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow("masked color", mask)


def rgb_callback(data):
    br2 = CvBridge()
    color_img = br2.imgmsg_to_cv2(data)
    color_img = cv2.cvtColor(color_img, cv2.COLOR_BGRA2BGR)
    color_img = imutils.resize(color_img, width=600)

    showColoredMask(color_img)

    cv2.imshow("rgb camera", color_img)
    cv2.waitKey(1)

def receive_message():

    # Tells rospy the name of the node.
    # Anonymous = True makes sure the node has a unique name. Random
    # numbers are added to the end of the name. 
    rospy.init_node('kinect_rgbcolormasking', anonymous=True)

    # Node is subscribing to the rgb/image_raw topic
    rospy.Subscriber('/kinect2/sd/image_color_rect', Image, rgb_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    receive_message()
