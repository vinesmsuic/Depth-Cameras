import pyrealsense2 as rs
import numpy as np
import math
import time
import cv2

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

#see L515 datasheet for depth and rgb streaming resolution!!
config.enable_stream(rs.stream.depth, depthwidth, depthheight, rs.format.z16, fps)  # depth

config.enable_stream(rs.stream.color, colorwidth, colorheight, rs.format.bgr8, fps) # rgb
"""
config.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, 63) # acceleration
config.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)  # gyro
"""
stream = pipeline.start(config)
depth_sensor = stream.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: " , depth_scale)
align_to = rs.stream.color
align = rs.align(align_to)

i=0

try:
    frame_count = 0
    start_time = time.time()
    while True:

        # Wait for a coherent pair of frames: depth and color
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
        #print(depth_frame.get_distance(int(depthwidth/2), int(depthheight/2)))

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image 
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)\

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))
        images = depth_colormap

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        #print(depth_image.shape)
        #print(color_image.shape)
        """
        #print IMU
        print("accel at frame {} at time {}: {}".format(str(frame_count), str(frame_time), str(accel_frame.as_motion_frame().get_motion_data())))
        print("gyro  at frame {} at time {}: {}".format(str(frame_count), str(frame_time), str(gyro_frame.as_motion_frame().get_motion_data())))
        """
        
        # Press 's' to save image
        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'):
            cv2.imwrite(f"{i}.jpg", color_image)
            cv2.imwrite(f"d{i}.png", depth_image)

            print(f"colored image {i}.jpg have been saved")
            #print(depth_image)
            #print(np.nanmin(depth_image))
            #print(np.percentile(depth_image,50))
            i += 1
        # Press esc or 'q' to close the image window
        elif key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
        
finally:
    # Stop streaming
    pipeline.stop()
