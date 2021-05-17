
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

YOU MUST USE THE FOLLOWING MATCHING PAIRS, according to the datasheet:
* Color 1920x1080, Depth 1024x768 (Operation Range 0.25 - 6m)
* Color 1280x720, Depth 640x480 (Operation Range 0.25 - 9m)
* Color 960x540, Depth 320x240 (Operation Range 0.25 - 9m)

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

