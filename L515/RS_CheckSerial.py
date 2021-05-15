import pyrealsense2 as rs

def find_L515_device_serial():
    ctx = rs.context()
    devices = ctx.query_devices()
    for dev in devices:
        if dev.get_info(rs.camera_info.name) == "Intel RealSense L515":
            print("Found L515 device:", dev.get_info(rs.camera_info.name))
            print("Serial number:",dev.get_info(rs.camera_info.serial_number))
        else:
            print("Not found")

find_L515_device_serial()
