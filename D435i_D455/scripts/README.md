# This folder is for ROS Scripts.

## Tested Enviroment
* ROS Version: ROS1 Medloic
* Realsense Version: (RS_SDK v2.41.0 + RS_ROS v2.2.21)


## Require Packages
* Require Package: cvbridge, rospy, message_filters

You can create a catkin package in `<your workspace>/src`
```shell
catkin_create_pkg opencv_task_handler image_transport cv_bridge sensor_msgs rospy roscpp std_msgs message_filters
```

## Common Mistakes

* To use the script, you need to set it executable.

```shell
sudo chmod +x yourfile.py
```

* Use USB 3.0 Port instead of 2.0 .


* Do `source ./devel/setup.bash` after each change on launch file.