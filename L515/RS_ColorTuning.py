import pyrealsense2 as rs
import numpy as np
import math
import time
import cv2
import imutils


def nothing(x):
    pass

device_id = 'f1061955'  # serial number of device

# Configure streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_device(device_id)

colorwidth = 1280
colorheight = 720
fps = 30

config.enable_stream(rs.stream.color, colorwidth, colorheight, rs.format.bgr8, fps) # rgb

# Start streaming
stream = pipeline.start(config)

try:
    # Create a window
    cv2.namedWindow('image')

    cv2.createTrackbar('HMin','image',0,179,nothing) # Hue is from 0-179 for Opencv
    cv2.createTrackbar('HMax','image',0,179,nothing)
    
    cv2.createTrackbar('SMin','image',0,255,nothing)
    cv2.createTrackbar('SMax','image',0,255,nothing)

    cv2.createTrackbar('VMin','image',0,255,nothing)
    cv2.createTrackbar('VMax','image',0,255,nothing)

    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('HMax', 'image', 179)
    cv2.setTrackbarPos('SMax', 'image', 255)
    cv2.setTrackbarPos('VMax', 'image', 255)

    # Initialize to check if HSV min/max value changes
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0

    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        color_image = np.asanyarray(color_frame.get_data())
        
        output = color_image
        color_image = imutils.resize(color_image, width=600)

        # get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin','image')
        sMin = cv2.getTrackbarPos('SMin','image')
        vMin = cv2.getTrackbarPos('VMin','image')

        hMax = cv2.getTrackbarPos('HMax','image')
        sMax = cv2.getTrackbarPos('SMax','image')
        vMax = cv2.getTrackbarPos('VMax','image')

        # Set minimum and max HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        # Create HSV Image and threshold into a range.
        hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(color_image,color_image, mask= mask)

        # Print if there is a change in HSV value
        if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
            print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax

        # Display output image
        cv2.imshow('image',output)

        waitTime = 33
        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(waitTime) & 0xFF == ord('q'):
            break
finally:
    # Stop streaming
    pipeline.stop()