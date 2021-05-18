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
fps = 30

config.enable_stream(rs.stream.color, colorwidth, colorheight, rs.format.bgr8, fps) # rgb


