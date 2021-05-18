import pyrealsense2 as rs
import numpy as np
import math
import time
import cv2
import imutils

device_id = 'f1061955'  # serial number of device

# Configure streams

pipeline = rs.pipeline()
config = rs.config()
config.enable_device(device_id)

colorwidth = 1280
colorheight = 720
depthwidth = 1024
depthheight = 768
fps = 30

# see L515 datasheet for depth and rgb streaming resolution!!

config.enable_stream(rs.stream.depth, depthwidth, depthheight,
                     rs.format.z16, fps)  # depth

config.enable_stream(rs.stream.color, colorwidth, colorheight,
                     rs.format.bgr8, fps)  # rgb
stream = pipeline.start(config)
depth_sensor = stream.get_device().first_depth_sensor()

# depth_scale = depth_sensor.get_depth_scale()
# print("Depth Scale is: " , depth_scale)

align_to = rs.stream.color
align = rs.align(align_to)

# Setting Color

colorLower = np.array([136, 100, 41])
colorUpper = np.array([179, 0xFF, 0xFF])

try:
    while True:
        
        frames = pipeline.wait_for_frames()

        # Align the depth frame to color frame
        aligned_frames = align.process(frames) 
        depth_frame = aligned_frames.get_depth_frame() 
        color_frame = aligned_frames.get_color_frame()

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image 
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)\

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))
        images = depth_colormap

        # Resize Color Image
        color_image = imutils.resize(color_image, width=600)


        images = imutils.resize(images, width=600)
        cv2.imshow('ColorMap', images)

        # Apply color tracking
        blurred = cv2.GaussianBlur(color_image, (11, 11), 0)  # eliminate noises
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # construct a mask for the color

        mask = cv2.inRange(hsv, colorLower, colorUpper)

        # perform a series of dilations and erosions to remove any small blobs left in the mask

        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current (x, y) center

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # only proceed if at least one contour was found

        if len(cnts) > 0:

            # find the largest contour in the mask, then use it to compute the minimum enclosing circle

            #c = max(cnts, key=cv2.contourArea)


            #Draw Rectangle
            for c in cnts:
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(color_image, (x,y), (x+w,y+h), (255, 0, 0), 2)

            #Draw Circle
            """
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # only proceed if the radius meets a minimum size

            if radius > 10:

                # draw the circle on the frame

                cv2.circle(color_image, (int(x), int(y)), int(radius), (0, 0xFF, 0xFF), 2)
            """

        # show the frame to our screen

        cv2.imshow('Color Tracker', color_image)
        cv2.imshow('Masked', mask)

        # if the 'q' key is pressed, stop the loop

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:

    # Stop streaming

    pipeline.stop()
