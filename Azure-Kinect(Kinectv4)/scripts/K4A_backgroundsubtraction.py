#!/usr/bin/env python

import rospy
import message_filters # To Achieve Multiple subscriber
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from cv_bridge import CvBridge
import cv2 #3.2.0
import imutils

class Kinect_Node(object):
    def __init__(self):

        rospy.init_node("kinect_sub_py", anonymous=True)

        #Reserved for 
        self.first_frame = None
        self.discard_counter = 0
        self.pub_frame1 = None
        self.distance = None

        self.loop_rate = rospy.Rate(60)

        #use CvBridge to convert between ROS and OpenCV images
        self.br = CvBridge()

        # Node is subscribing to the topic
        self.rgb_sub = message_filters.Subscriber('rgb/image_raw', Image)
        self.depth_sub = message_filters.Subscriber('depth_to_rgb/image_raw', Image)

        # Node is publishing to the topic
        self.rgb_pub = rospy.Publisher('/rgb/contours', Image, queue_size=10)
        self.distance_pub = rospy.Publisher('/rgb/contours/distance', Float32, queue_size=10)

    def callback(self, ros_rgb, ros_depth):

        #for getting fps
        timer = cv2.getTickCount()
        
        #convert ROS image message to OpenCV image 
        depth_frame = self.br.imgmsg_to_cv2(ros_depth, desired_encoding="32FC1")
        rgb_frame = self.br.imgmsg_to_cv2(ros_rgb, "bgr8")

        #resize image
        depth_frame = imutils.resize(depth_frame, width=600)
        rgb_frame = imutils.resize(rgb_frame, width=600)
        
        depth_frame = cv2.cvtColor(depth_frame, cv2.COLOR_GRAY2BGR)
        rgb_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_BGRA2BGR)

        diff_mask = self.getDiff(rgb_frame)
        if diff_mask is not None:
            blob_distance = cv2.bitwise_and(depth_frame, depth_frame, mask=diff_mask)
            if(blob_distance.flatten().max() > 0.1):
                #possible_distance = np.median(blob_distance.flatten())
                possible_distance = blob_distance.flatten()
                possible_distance = possible_distance[possible_distance != 0.0]
                possible_distance = np.percentile(possible_distance,90)
                #rospy.loginfo(blob_distance)
                rospy.loginfo("possible_distance: %s", possible_distance)
                self.distance = possible_distance
        
        #If we want to stablize, don't use imshow and waitKey. Use a publisher to send the data out and use rqt_gui to see the frame.
        #cv2.imshow("depth camera", depth_frame)
        #cv2.imshow("rgb camera", rgb_frame)

        fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
        rospy.loginfo("The fps is: %s", fps)
        
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    self.first_frame = None
        
    
    def getDiff(self, frame):

        #handle camera not init problem
        if self.discard_counter < 25:
            self.discard_counter+=1
            return None
        
        #store background to subtract
        if self.first_frame is None:
            self.first_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.first_frame = cv2.GaussianBlur(self.first_frame, (3,3), 0)
            return None
        else:
            first_frame = self.first_frame
            es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,4))
            kernel = np.ones((5,5), np.uint8)
            this_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            this_frame = cv2.GaussianBlur(this_frame, (3,3), 0)
            diff = cv2.absdiff(first_frame, this_frame)
            diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)[1]
            diff = cv2.dilate(diff, es, iterations=2)
            diff = cv2.erode(diff, None, iterations=1)
            
            _, cnts, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv2.contourArea(c) < 1500:
                    continue
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(this_frame, (x,y), (x+w, y+h), (0,255,0), 2)
            this_frame = cv2.cvtColor(this_frame, cv2.COLOR_GRAY2BGR)
            self.pub_frame1 = self.br.cv2_to_imgmsg(this_frame, encoding="bgr8")
            #cv2.imshow("Contours", this_frame)
            #cv2.imshow("Diff", diff)
            return diff

    def start(self):

        # Tells rospy the name of the node.
        # Anonymous = True makes sure the node has a unique name. Random
        # numbers are added to the end of the name. 

        ts = message_filters.ApproximateTimeSynchronizer([self.rgb_sub, self.depth_sub], 10, 0.01)
        ts.registerCallback(self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        #rospy.spin()
        
        while not rospy.is_shutdown():
            if self.pub_frame1 is not None:
                self.rgb_pub.publish(self.pub_frame1)
            if self.distance is not None:
                self.distance_pub.publish(self.distance)
            self.loop_rate.sleep()
        

if __name__ == '__main__':
    my_node = Kinect_Node()
    my_node.start()