# ROS driver usage - Start the camera node

```shell
roslaunch realsense2_camera rs_camera.launch
```

D435i and D455 should work using the same program.

Supported stream for d435i:
```
$ rs-enumerate-devices 
Device info: 
    Name                          : 	Intel RealSense D435I
    Serial Number                 : 	036522072893
    Firmware Version              : 	05.12.09.00
    Recommended Firmware Version  : 	05.12.13.50
    Physical Port                 : 	/sys/devices/3610000.xhci/usb2/2-1/2-1:1.0/video4linux/video0
    Debug Op Code                 : 	15
    Advanced Mode                 : 	YES
    Product Id                    : 	0B3A
    Camera Locked                 : 	YES
    Usb Type Descriptor           : 	3.2
    Product Line                  : 	D400
    Asic Serial Number            : 	039223051460
    Firmware Update Id            : 	039223051460

Stream Profiles supported by Stereo Module
 Supported modes:
    stream       resolution      fps       format   
    Infrared 1	  1280x800	@ 30Hz	   Y8
    Infrared 1	  1280x800	@ 25Hz	   Y16
    Infrared 1	  1280x800	@ 15Hz	   Y16
    Infrared 1	  1280x800	@ 15Hz	   Y8
    Infrared 1	  1280x720	@ 30Hz	   Y8
    Infrared 1	  1280x720	@ 15Hz	   Y8
    Infrared 1	  1280x720	@ 6Hz	   Y8
    Infrared 1	  848x480	@ 90Hz	   Y8
    Infrared 1	  848x480	@ 60Hz	   Y8
    Infrared 1	  848x480	@ 30Hz	   Y8
    Infrared 1	  848x480	@ 15Hz	   Y8
    Infrared 1	  848x480	@ 6Hz	   Y8
    Infrared 1	  848x100	@ 300Hz	   Y8
    Infrared 1	  848x100	@ 100Hz	   Y8
    Infrared 1	  640x480	@ 90Hz	   Y8
    Infrared 1	  640x480	@ 60Hz	   Y8
    Infrared 1	  640x480	@ 30Hz	   Y8
    Infrared 1	  640x480	@ 15Hz	   Y8
    Infrared 1	  640x480	@ 6Hz	   Y8
    Infrared 1	  640x400	@ 25Hz	   Y16
    Infrared 1	  640x400	@ 15Hz	   Y16
    Infrared 1	  640x360	@ 90Hz	   Y8
    Infrared 1	  640x360	@ 60Hz	   Y8
    Infrared 1	  640x360	@ 30Hz	   Y8
    Infrared 1	  640x360	@ 15Hz	   Y8
    Infrared 1	  640x360	@ 6Hz	   Y8
    Infrared 1	  480x270	@ 90Hz	   Y8
    Infrared 1	  480x270	@ 60Hz	   Y8
    Infrared 1	  480x270	@ 30Hz	   Y8
    Infrared 1	  480x270	@ 15Hz	   Y8
    Infrared 1	  480x270	@ 6Hz	   Y8
    Infrared 1	  424x240	@ 90Hz	   Y8
    Infrared 1	  424x240	@ 60Hz	   Y8
    Infrared 1	  424x240	@ 30Hz	   Y8
    Infrared 1	  424x240	@ 15Hz	   Y8
    Infrared 1	  424x240	@ 6Hz	   Y8
    Infrared 1	  256x144	@ 300Hz	   Y8
    Infrared 1	  256x144	@ 90Hz	   Y8
    Infrared 2	  1280x800	@ 30Hz	   Y8
    Infrared 2	  1280x800	@ 25Hz	   Y16
    Infrared 2	  1280x800	@ 15Hz	   Y16
    Infrared 2	  1280x800	@ 15Hz	   Y8
    Infrared 2	  1280x720	@ 30Hz	   Y8
    Infrared 2	  1280x720	@ 15Hz	   Y8
    Infrared 2	  1280x720	@ 6Hz	   Y8
    Infrared 2	  848x480	@ 90Hz	   Y8
    Infrared 2	  848x480	@ 60Hz	   Y8
    Infrared 2	  848x480	@ 30Hz	   Y8
    Infrared 2	  848x480	@ 15Hz	   Y8
    Infrared 2	  848x480	@ 6Hz	   Y8
    Infrared 2	  848x100	@ 300Hz	   Y8
    Infrared 2	  848x100	@ 100Hz	   Y8
    Infrared 2	  640x480	@ 90Hz	   Y8
    Infrared 2	  640x480	@ 60Hz	   Y8
    Infrared 2	  640x480	@ 30Hz	   Y8
    Infrared 2	  640x480	@ 15Hz	   Y8
    Infrared 2	  640x480	@ 6Hz	   Y8
    Infrared 2	  640x400	@ 25Hz	   Y16
    Infrared 2	  640x400	@ 15Hz	   Y16
    Infrared 2	  640x360	@ 90Hz	   Y8
    Infrared 2	  640x360	@ 60Hz	   Y8
    Infrared 2	  640x360	@ 30Hz	   Y8
    Infrared 2	  640x360	@ 15Hz	   Y8
    Infrared 2	  640x360	@ 6Hz	   Y8
    Infrared 2	  480x270	@ 90Hz	   Y8
    Infrared 2	  480x270	@ 60Hz	   Y8
    Infrared 2	  480x270	@ 30Hz	   Y8
    Infrared 2	  480x270	@ 15Hz	   Y8
    Infrared 2	  480x270	@ 6Hz	   Y8
    Infrared 2	  424x240	@ 90Hz	   Y8
    Infrared 2	  424x240	@ 60Hz	   Y8
    Infrared 2	  424x240	@ 30Hz	   Y8
    Infrared 2	  424x240	@ 15Hz	   Y8
    Infrared 2	  424x240	@ 6Hz	   Y8
    Infrared 2	  256x144	@ 300Hz	   Y8
    Infrared 2	  256x144	@ 90Hz	   Y8
    Depth	  1280x720	@ 30Hz	   Z16
    Depth	  1280x720	@ 15Hz	   Z16
    Depth	  1280x720	@ 6Hz	   Z16
    Depth	  848x480	@ 90Hz	   Z16
    Depth	  848x480	@ 60Hz	   Z16
    Depth	  848x480	@ 30Hz	   Z16
    Depth	  848x480	@ 15Hz	   Z16
    Depth	  848x480	@ 6Hz	   Z16
    Depth	  848x100	@ 300Hz	   Z16
    Depth	  848x100	@ 100Hz	   Z16
    Depth	  640x480	@ 90Hz	   Z16
    Depth	  640x480	@ 60Hz	   Z16
    Depth	  640x480	@ 30Hz	   Z16
    Depth	  640x480	@ 15Hz	   Z16
    Depth	  640x480	@ 6Hz	   Z16
    Depth	  640x360	@ 90Hz	   Z16
    Depth	  640x360	@ 60Hz	   Z16
    Depth	  640x360	@ 30Hz	   Z16
    Depth	  640x360	@ 15Hz	   Z16
    Depth	  640x360	@ 6Hz	   Z16
    Depth	  480x270	@ 90Hz	   Z16
    Depth	  480x270	@ 60Hz	   Z16
    Depth	  480x270	@ 30Hz	   Z16
    Depth	  480x270	@ 15Hz	   Z16
    Depth	  480x270	@ 6Hz	   Z16
    Depth	  424x240	@ 90Hz	   Z16
    Depth	  424x240	@ 60Hz	   Z16
    Depth	  424x240	@ 30Hz	   Z16
    Depth	  424x240	@ 15Hz	   Z16
    Depth	  424x240	@ 6Hz	   Z16
    Depth	  256x144	@ 300Hz	   Z16
    Depth	  256x144	@ 90Hz	   Z16

Stream Profiles supported by RGB Camera
 Supported modes:
    stream       resolution      fps       format   
    Color	  1920x1080	@ 30Hz	   RGB8
    Color	  1920x1080	@ 30Hz	   RAW16
    Color	  1920x1080	@ 30Hz	   Y16
    Color	  1920x1080	@ 30Hz	   BGRA8
    Color	  1920x1080	@ 30Hz	   RGBA8
    Color	  1920x1080	@ 30Hz	   BGR8
    Color	  1920x1080	@ 30Hz	   YUYV
    Color	  1920x1080	@ 15Hz	   RGB8
    Color	  1920x1080	@ 15Hz	   Y16
    Color	  1920x1080	@ 15Hz	   BGRA8
    Color	  1920x1080	@ 15Hz	   RGBA8
    Color	  1920x1080	@ 15Hz	   BGR8
    Color	  1920x1080	@ 15Hz	   YUYV
    Color	  1920x1080	@ 6Hz	   RGB8
    Color	  1920x1080	@ 6Hz	   Y16
    Color	  1920x1080	@ 6Hz	   BGRA8
    Color	  1920x1080	@ 6Hz	   RGBA8
    Color	  1920x1080	@ 6Hz	   BGR8
    Color	  1920x1080	@ 6Hz	   YUYV
    Color	  1280x720	@ 30Hz	   RGB8
    Color	  1280x720	@ 30Hz	   Y16
    Color	  1280x720	@ 30Hz	   BGRA8
    Color	  1280x720	@ 30Hz	   RGBA8
    Color	  1280x720	@ 30Hz	   BGR8
    Color	  1280x720	@ 30Hz	   YUYV
    Color	  1280x720	@ 15Hz	   RGB8
    Color	  1280x720	@ 15Hz	   Y16
    Color	  1280x720	@ 15Hz	   BGRA8
    Color	  1280x720	@ 15Hz	   RGBA8
    Color	  1280x720	@ 15Hz	   BGR8
    Color	  1280x720	@ 15Hz	   YUYV
    Color	  1280x720	@ 6Hz	   RGB8
    Color	  1280x720	@ 6Hz	   Y16
    Color	  1280x720	@ 6Hz	   BGRA8
    Color	  1280x720	@ 6Hz	   RGBA8
    Color	  1280x720	@ 6Hz	   BGR8
    Color	  1280x720	@ 6Hz	   YUYV
    Color	  960x540	@ 60Hz	   RGB8
    Color	  960x540	@ 60Hz	   Y16
    Color	  960x540	@ 60Hz	   BGRA8
    Color	  960x540	@ 60Hz	   RGBA8
    Color	  960x540	@ 60Hz	   BGR8
    Color	  960x540	@ 60Hz	   YUYV
    Color	  960x540	@ 30Hz	   RGB8
    Color	  960x540	@ 30Hz	   Y16
    Color	  960x540	@ 30Hz	   BGRA8
    Color	  960x540	@ 30Hz	   RGBA8
    Color	  960x540	@ 30Hz	   BGR8
    Color	  960x540	@ 30Hz	   YUYV
    Color	  960x540	@ 15Hz	   RGB8
    Color	  960x540	@ 15Hz	   Y16
    Color	  960x540	@ 15Hz	   BGRA8
    Color	  960x540	@ 15Hz	   RGBA8
    Color	  960x540	@ 15Hz	   BGR8
    Color	  960x540	@ 15Hz	   YUYV
    Color	  960x540	@ 6Hz	   RGB8
    Color	  960x540	@ 6Hz	   Y16
    Color	  960x540	@ 6Hz	   BGRA8
    Color	  960x540	@ 6Hz	   RGBA8
    Color	  960x540	@ 6Hz	   BGR8
    Color	  960x540	@ 6Hz	   YUYV
    Color	  848x480	@ 60Hz	   RGB8
    Color	  848x480	@ 60Hz	   Y16
    Color	  848x480	@ 60Hz	   BGRA8
    Color	  848x480	@ 60Hz	   RGBA8
    Color	  848x480	@ 60Hz	   BGR8
    Color	  848x480	@ 60Hz	   YUYV
    Color	  848x480	@ 30Hz	   RGB8
    Color	  848x480	@ 30Hz	   Y16
    Color	  848x480	@ 30Hz	   BGRA8
    Color	  848x480	@ 30Hz	   RGBA8
    Color	  848x480	@ 30Hz	   BGR8
    Color	  848x480	@ 30Hz	   YUYV
    Color	  848x480	@ 15Hz	   RGB8
    Color	  848x480	@ 15Hz	   Y16
    Color	  848x480	@ 15Hz	   BGRA8
    Color	  848x480	@ 15Hz	   RGBA8
    Color	  848x480	@ 15Hz	   BGR8
    Color	  848x480	@ 15Hz	   YUYV
    Color	  848x480	@ 6Hz	   RGB8
    Color	  848x480	@ 6Hz	   Y16
    Color	  848x480	@ 6Hz	   BGRA8
    Color	  848x480	@ 6Hz	   RGBA8
    Color	  848x480	@ 6Hz	   BGR8
    Color	  848x480	@ 6Hz	   YUYV
    Color	  640x480	@ 60Hz	   RGB8
    Color	  640x480	@ 60Hz	   Y16
    Color	  640x480	@ 60Hz	   BGRA8
    Color	  640x480	@ 60Hz	   RGBA8
    Color	  640x480	@ 60Hz	   BGR8
    Color	  640x480	@ 60Hz	   YUYV
    Color	  640x480	@ 30Hz	   RGB8
    Color	  640x480	@ 30Hz	   Y16
    Color	  640x480	@ 30Hz	   BGRA8
    Color	  640x480	@ 30Hz	   RGBA8
    Color	  640x480	@ 30Hz	   BGR8
    Color	  640x480	@ 30Hz	   YUYV
    Color	  640x480	@ 15Hz	   RGB8
    Color	  640x480	@ 15Hz	   Y16
    Color	  640x480	@ 15Hz	   BGRA8
    Color	  640x480	@ 15Hz	   RGBA8
    Color	  640x480	@ 15Hz	   BGR8
    Color	  640x480	@ 15Hz	   YUYV
    Color	  640x480	@ 6Hz	   RGB8
    Color	  640x480	@ 6Hz	   Y16
    Color	  640x480	@ 6Hz	   BGRA8
    Color	  640x480	@ 6Hz	   RGBA8
    Color	  640x480	@ 6Hz	   BGR8
    Color	  640x480	@ 6Hz	   YUYV
    Color	  640x360	@ 60Hz	   RGB8
    Color	  640x360	@ 60Hz	   Y16
    Color	  640x360	@ 60Hz	   BGRA8
    Color	  640x360	@ 60Hz	   RGBA8
    Color	  640x360	@ 60Hz	   BGR8
    Color	  640x360	@ 60Hz	   YUYV
    Color	  640x360	@ 30Hz	   RGB8
    Color	  640x360	@ 30Hz	   Y16
    Color	  640x360	@ 30Hz	   BGRA8
    Color	  640x360	@ 30Hz	   RGBA8
    Color	  640x360	@ 30Hz	   BGR8
    Color	  640x360	@ 30Hz	   YUYV
    Color	  640x360	@ 15Hz	   RGB8
    Color	  640x360	@ 15Hz	   Y16
    Color	  640x360	@ 15Hz	   BGRA8
    Color	  640x360	@ 15Hz	   RGBA8
    Color	  640x360	@ 15Hz	   BGR8
    Color	  640x360	@ 15Hz	   YUYV
    Color	  640x360	@ 6Hz	   RGB8
    Color	  640x360	@ 6Hz	   Y16
    Color	  640x360	@ 6Hz	   BGRA8
    Color	  640x360	@ 6Hz	   RGBA8
    Color	  640x360	@ 6Hz	   BGR8
    Color	  640x360	@ 6Hz	   YUYV
    Color	  424x240	@ 60Hz	   RGB8
    Color	  424x240	@ 60Hz	   Y16
    Color	  424x240	@ 60Hz	   BGRA8
    Color	  424x240	@ 60Hz	   RGBA8
    Color	  424x240	@ 60Hz	   BGR8
    Color	  424x240	@ 60Hz	   YUYV
    Color	  424x240	@ 30Hz	   RGB8
    Color	  424x240	@ 30Hz	   Y16
    Color	  424x240	@ 30Hz	   BGRA8
    Color	  424x240	@ 30Hz	   RGBA8
    Color	  424x240	@ 30Hz	   BGR8
    Color	  424x240	@ 30Hz	   YUYV
    Color	  424x240	@ 15Hz	   RGB8
    Color	  424x240	@ 15Hz	   Y16
    Color	  424x240	@ 15Hz	   BGRA8
    Color	  424x240	@ 15Hz	   RGBA8
    Color	  424x240	@ 15Hz	   BGR8
    Color	  424x240	@ 15Hz	   YUYV
    Color	  424x240	@ 6Hz	   RGB8
    Color	  424x240	@ 6Hz	   Y16
    Color	  424x240	@ 6Hz	   BGRA8
    Color	  424x240	@ 6Hz	   RGBA8
    Color	  424x240	@ 6Hz	   BGR8
    Color	  424x240	@ 6Hz	   YUYV
    Color	  320x240	@ 60Hz	   RGB8
    Color	  320x240	@ 60Hz	   Y16
    Color	  320x240	@ 60Hz	   BGRA8
    Color	  320x240	@ 60Hz	   RGBA8
    Color	  320x240	@ 60Hz	   BGR8
    Color	  320x240	@ 60Hz	   YUYV
    Color	  320x240	@ 30Hz	   RGB8
    Color	  320x240	@ 30Hz	   Y16
    Color	  320x240	@ 30Hz	   BGRA8
    Color	  320x240	@ 30Hz	   RGBA8
    Color	  320x240	@ 30Hz	   BGR8
    Color	  320x240	@ 30Hz	   YUYV
    Color	  320x240	@ 6Hz	   RGB8
    Color	  320x240	@ 6Hz	   Y16
    Color	  320x240	@ 6Hz	   BGRA8
    Color	  320x240	@ 6Hz	   RGBA8
    Color	  320x240	@ 6Hz	   BGR8
    Color	  320x240	@ 6Hz	   YUYV
    Color	  320x180	@ 60Hz	   RGB8
    Color	  320x180	@ 60Hz	   Y16
    Color	  320x180	@ 60Hz	   BGRA8
    Color	  320x180	@ 60Hz	   RGBA8
    Color	  320x180	@ 60Hz	   BGR8
    Color	  320x180	@ 60Hz	   YUYV
    Color	  320x180	@ 30Hz	   RGB8
    Color	  320x180	@ 30Hz	   Y16
    Color	  320x180	@ 30Hz	   BGRA8
    Color	  320x180	@ 30Hz	   RGBA8
    Color	  320x180	@ 30Hz	   BGR8
    Color	  320x180	@ 30Hz	   YUYV
    Color	  320x180	@ 6Hz	   RGB8
    Color	  320x180	@ 6Hz	   Y16
    Color	  320x180	@ 6Hz	   BGRA8
    Color	  320x180	@ 6Hz	   RGBA8
    Color	  320x180	@ 6Hz	   BGR8
    Color	  320x180	@ 6Hz	   YUYV

Stream Profiles supported by Motion Module
 Supported modes:
    stream       resolution      fps       format   
    Accel	 N/A		@ 250Hz	   MOTION_XYZ32F
    Accel	 N/A		@ 63Hz	   MOTION_XYZ32F
    Gyro	 N/A		@ 400Hz	   MOTION_XYZ32F
    Gyro	 N/A		@ 200Hz	   MOTION_XYZ32F

```
