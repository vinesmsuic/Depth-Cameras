import pyrealsense2 as rs
import numpy as np
import cv2

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
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        color_image = np.asanyarray(color_frame.get_data())
        cv2.imshow('image', color_image)
        
        
        key = cv2.waitKey(1)
        # Press esc or 'q' to close the image window
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:
    # Stop streaming
    pipeline.stop()

