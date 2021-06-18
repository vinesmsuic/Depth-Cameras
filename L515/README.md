
L515 is a LiDAR, but it can also act as a Depth and RGB sensor.

To get device serial number
```shell
rs-enumerate-devices | grep Serial
```


To use the ros driver:
```shell
roslaunch realsense2_camera rs_camera.launch enable_infra:=true
```
It also tell you the serial number. 
looking for the serial number in the log printed to screen under "[INFO][...]Device Serial No:".

* As per the L515 datasheet, 640x480 is not a supported RGB resolution.
* So you would not get Color topics from original Realsense ROS driver.

YOU MUST USE THE FOLLOWING MATCHING stream set. You can refer to `rs-enumerate-devices`.
```
$ rs-enumerate-devices
Device info:
    Name                          :     Intel RealSense L515
    Serial Number                 :     f1061955
    Firmware Version              :     01.05.08.01
    Recommended Firmware Version  :     01.05.05.00
    Physical Port                 :     2-3.3-3
    Debug Op Code                 :     15
    Product Id                    :     0B64
    Camera Locked                 :     YES
    Usb Type Descriptor           :     3.2
    Product Line                  :     L500
    Asic Serial Number            :     0003ba80b330
    Firmware Update Id            :     0003ba80b330

Stream Profiles supported by L500 Depth Sensor
 Supported modes:
    stream       resolution      fps       format
    Confidence    1024x768      @ 30Hz     RAW8
    Confidence    640x480       @ 30Hz     RAW8
    Confidence    320x240       @ 30Hz     RAW8
    Infrared      1024x768      @ 30Hz     Y8
    Infrared      640x480       @ 30Hz     Y8
    Infrared      320x240       @ 30Hz     Y8
    Depth         1024x768      @ 30Hz     Z16
    Depth         640x480       @ 30Hz     Z16
    Depth         320x240       @ 30Hz     Z16

Stream Profiles supported by RGB Camera
 Supported modes:
    stream       resolution      fps       format
    Color         1920x1080     @ 30Hz     RGB8
    Color         1920x1080     @ 30Hz     Y16
    Color         1920x1080     @ 30Hz     BGRA8
    Color         1920x1080     @ 30Hz     RGBA8
    Color         1920x1080     @ 30Hz     BGR8
    Color         1920x1080     @ 30Hz     YUYV
    Color         1920x1080     @ 15Hz     RGB8
    Color         1920x1080     @ 15Hz     Y16
    Color         1920x1080     @ 15Hz     BGRA8
    Color         1920x1080     @ 15Hz     RGBA8
    Color         1920x1080     @ 15Hz     BGR8
    Color         1920x1080     @ 15Hz     YUYV
    Color         1920x1080     @ 6Hz      RGB8
    Color         1920x1080     @ 6Hz      Y16
    Color         1920x1080     @ 6Hz      BGRA8
    Color         1920x1080     @ 6Hz      RGBA8
    Color         1920x1080     @ 6Hz      BGR8
    Color         1920x1080     @ 6Hz      YUYV
    Color         1280x720      @ 60Hz     RGB8
    Color         1280x720      @ 60Hz     Y16
    Color         1280x720      @ 60Hz     BGRA8
    Color         1280x720      @ 60Hz     RGBA8
    Color         1280x720      @ 60Hz     BGR8
    Color         1280x720      @ 60Hz     YUYV
    Color         1280x720      @ 30Hz     RGB8
    Color         1280x720      @ 30Hz     Y16
    Color         1280x720      @ 30Hz     BGRA8
    Color         1280x720      @ 30Hz     RGBA8
    Color         1280x720      @ 30Hz     BGR8
    Color         1280x720      @ 30Hz     YUYV
    Color         1280x720      @ 15Hz     RGB8
    Color         1280x720      @ 15Hz     Y16
    Color         1280x720      @ 15Hz     BGRA8
    Color         1280x720      @ 15Hz     RGBA8
    Color         1280x720      @ 15Hz     BGR8
    Color         1280x720      @ 15Hz     YUYV
    Color         1280x720      @ 6Hz      RGB8
    Color         1280x720      @ 6Hz      Y16
    Color         1280x720      @ 6Hz      BGRA8
    Color         1280x720      @ 6Hz      RGBA8
    Color         1280x720      @ 6Hz      BGR8
    Color         1280x720      @ 6Hz      YUYV
    Color         960x540       @ 60Hz     RGB8
    Color         960x540       @ 60Hz     Y16
    Color         960x540       @ 60Hz     BGRA8
    Color         960x540       @ 60Hz     RGBA8
    Color         960x540       @ 60Hz     BGR8
    Color         960x540       @ 60Hz     YUYV
    Color         960x540       @ 30Hz     RGB8
    Color         960x540       @ 30Hz     Y16
    Color         960x540       @ 30Hz     BGRA8
    Color         960x540       @ 30Hz     RGBA8
    Color         960x540       @ 30Hz     BGR8
    Color         960x540       @ 30Hz     YUYV
    Color         960x540       @ 15Hz     RGB8
    Color         960x540       @ 15Hz     Y16
    Color         960x540       @ 15Hz     BGRA8
    Color         960x540       @ 15Hz     RGBA8
    Color         960x540       @ 15Hz     BGR8
    Color         960x540       @ 15Hz     YUYV
    Color         960x540       @ 6Hz      RGB8
    Color         960x540       @ 6Hz      Y16
    Color         960x540       @ 6Hz      BGRA8
    Color         960x540       @ 6Hz      RGBA8
    Color         960x540       @ 6Hz      BGR8
    Color         960x540       @ 6Hz      YUYV
    Color         640x480       @ 60Hz     RGB8
    Color         640x480       @ 60Hz     Y16
    Color         640x480       @ 60Hz     BGRA8
    Color         640x480       @ 60Hz     RGBA8
    Color         640x480       @ 60Hz     BGR8
    Color         640x480       @ 60Hz     YUYV
    Color         640x480       @ 30Hz     RGB8
    Color         640x480       @ 30Hz     Y16
    Color         640x480       @ 30Hz     BGRA8
    Color         640x480       @ 30Hz     RGBA8
    Color         640x480       @ 30Hz     BGR8
    Color         640x480       @ 30Hz     YUYV
    Color         640x480       @ 15Hz     RGB8
    Color         640x480       @ 15Hz     Y16
    Color         640x480       @ 15Hz     BGRA8
    Color         640x480       @ 15Hz     RGBA8
    Color         640x480       @ 15Hz     BGR8
    Color         640x480       @ 15Hz     YUYV
    Color         640x480       @ 6Hz      RGB8
    Color         640x480       @ 6Hz      Y16
    Color         640x480       @ 6Hz      BGRA8
    Color         640x480       @ 6Hz      RGBA8
    Color         640x480       @ 6Hz      BGR8
    Color         640x480       @ 6Hz      YUYV
    Color         640x360       @ 60Hz     RGB8
    Color         640x360       @ 60Hz     Y16
    Color         640x360       @ 60Hz     BGRA8
    Color         640x360       @ 60Hz     RGBA8
    Color         640x360       @ 60Hz     BGR8
    Color         640x360       @ 60Hz     YUYV
    Color         640x360       @ 30Hz     RGB8
    Color         640x360       @ 30Hz     Y16
    Color         640x360       @ 30Hz     BGRA8
    Color         640x360       @ 30Hz     RGBA8
    Color         640x360       @ 30Hz     BGR8
    Color         640x360       @ 30Hz     YUYV
    Color         640x360       @ 15Hz     RGB8
    Color         640x360       @ 15Hz     Y16
    Color         640x360       @ 15Hz     BGRA8
    Color         640x360       @ 15Hz     RGBA8
    Color         640x360       @ 15Hz     BGR8
    Color         640x360       @ 15Hz     YUYV
    Color         640x360       @ 6Hz      RGB8
    Color         640x360       @ 6Hz      Y16
    Color         640x360       @ 6Hz      BGRA8
    Color         640x360       @ 6Hz      RGBA8
    Color         640x360       @ 6Hz      BGR8
    Color         640x360       @ 6Hz      YUYV

Stream Profiles supported by Motion Module
 Supported modes:
    stream       resolution      fps       format
    Accel        N/A            @ 400Hz    MOTION_XYZ32F
    Accel        N/A            @ 200Hz    MOTION_XYZ32F
    Accel        N/A            @ 100Hz    MOTION_XYZ32F
    Gyro         N/A            @ 400Hz    MOTION_XYZ32F
    Gyro         N/A            @ 200Hz    MOTION_XYZ32F
    Gyro         N/A            @ 100Hz    MOTION_XYZ32F


```


Note you need to modify the launch file of original Realsense ROS driver because the resolution of RGB is different in L515.

```xml
<!--change resolution of color-->
  <arg name="color_width"         default="1280"/>
  <arg name="color_height"        default="720"/>
  <arg name="enable_color"        default="true"/>

<!-- If you need Color-Align-Depth topics, change the below -->

<!--enable IMU -->
  <arg name="enable_gyro"         default="true"/>
  <arg name="enable_accel"        default="true"/>
<!-- enable IMU angluar and accerlate topics -->
 <arg name="unite_imu_method"      default="copy"/>

<!-- sync IMU and camera-->
 <arg name="enable_sync"           default="true"/>   
<!-- align depth -->
 <arg name="align_depth"               default="true"/>
<!-- enable infra-->
 <arg name="enable_infra"        default="true"/>
```

* SOURCE YOUR FILE AFTER MODIFYING THE LAUNCH FILE, or simply rebuild by `catkin_make`, otherwise there could be error

```
./devel/setup.bash
```



* [Reference: Realsense ros don't run with realsense LiDar L515](https://github.com/IntelRealSense/realsense-ros/issues/1348)

