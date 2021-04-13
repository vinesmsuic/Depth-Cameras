
L515 is a LiDAR, but it can also act as a Depth and RGB sensor.

To use the ros driver:
```shell
roslaunch realsense2_camera rs_camera.launch enable_infra:=true
```

Note you need to modify the launch file of original Realsense ROS driver because the resolution of RGB is different in L515.

```xml
<!--change resolution of color-->
  <arg name="color_width"         default="1280"/>
  <arg name="color_height"        default="720"/>
  <arg name="enable_color"        default="true"/>

<!--enable IMU -->
  <arg name="enable_gyro"         default="true"/>
  <arg name="enable_accel"        default="true"/>
<!-- enable IMU angluar and accerlate topics -->
 <arg name="unite_imu_method"      default="copy"/>
<!-- sync IMU and camera-->
 arg name="enable_sync"           default="true"/>   
<!-- align depth -->
 <arg name="align_depth"               default="true"/>
<!-- enable infra-->
 <arg name="enable_infra"        default="true"/>
```

[Realsense ros don't run with realsense LiDar L515](https://github.com/IntelRealSense/realsense-ros/issues/1348)