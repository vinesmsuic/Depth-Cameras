#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 #3.2.0
import imutils

def get_distance(frame):
    img_height = frame.shape[0]
    img_width = frame.shape[1]
    x_center = img_width/2
    y_center = img_height/2
    #rospy.loginfo("The center pixel value is: %s", frame[y_center][x_center])
    distance = float(frame[y_center][x_center])*100.0
    distance_arr = frame[y_center-10:y_center+11,x_center-10:x_center+11]
    distance_arr = distance_arr.flatten()
    median = np.median(distance_arr)
    rospy.loginfo("The median distance is: %s cm", median*100.0)
    rospy.loginfo("The distance of center pixel is: %s cm", distance)

    return distance

def draw_crosshair(frame, crosshair_size=5, crosshair_color=(255,0,0), stroke=1):
    img_height = frame.shape[0]
    img_width = frame.shape[1]
    x_center = img_width/2
    y_center = img_height/2
    cv2.line(frame, (x_center-crosshair_size,y_center-crosshair_size), (x_center+crosshair_size,y_center+crosshair_size), crosshair_color, stroke)
    cv2.line(frame, (x_center+crosshair_size,y_center-crosshair_size), (x_center-crosshair_size,y_center+crosshair_size), crosshair_color, stroke)
    cv2.rectangle(frame, (x_center-crosshair_size,y_center-crosshair_size), (x_center+crosshair_size,y_center+crosshair_size), (255,0,0), 1)

def callback(data):

    #use CvBridge to convert between ROS and OpenCV images
    br = CvBridge()

    #convert ROS image message to OpenCV image 
    current_frame = br.imgmsg_to_cv2(data, desired_encoding="32FC1")

    #resize image
    current_frame = imutils.resize(current_frame, width=600)
    current_frame = cv2.GaussianBlur(current_frame, (5,5) , 0)

    n_bgr_img = cv2.cvtColor(current_frame, cv2.COLOR_GRAY2BGR)
    
    distance = get_distance(current_frame)

    bgr_img = cv2.cvtColor(current_frame, cv2.COLOR_GRAY2BGR) 

    draw_crosshair(bgr_img, crosshair_size=10, crosshair_color=(0,0,255), stroke=1)

    if(distance != 0.0):
        cv2.putText(bgr_img, str(distance) + " cm", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA, False)
    else:
        cv2.putText(bgr_img, "Too Close/Far! Out of Range!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA, False)

    cv2.imshow("depth camera", bgr_img)

    cv2.imshow("depth camera (no filter)", n_bgr_img)

    cv2.waitKey(1)



def receive_message():

    # Tells rospy the name of the node.
    # Anonymous = True makes sure the node has a unique name. Random
    # numbers are added to the end of the name. 
    rospy.init_node('kinect_sub_py', anonymous=True)

    # Node is subscribing to the /depth_to_rgb/image_raw topic
    rospy.Subscriber('depth_to_rgb/image_raw', Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    receive_message()