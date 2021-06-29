# Common



## RGB+Depth Require Packages

* Require Package: `cvbridge`, `rospy`, `message_filters`

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

* Do `source ./devel/setup.bash` after each `catkin_make`.





# Configure Parameters of Camera

```powershell
rosrun rqt_reconfigure rqt_reconfigure
```





# For Video Analysis

## [rosbag usage](http://wiki.ros.org/rosbag/Commandline)


### Record
```shell
rosbag record <topic-names> -O <output filename>
```

#### Quick examples to record some topics of cameras:
* Start the camera topics, then start record a bag:

L515
```shell
roslaunch realsense2_camera rs_camera.launch enable_infra:=true
rosbag record camera/color/image_raw camera/aligned_depth_to_color/image_raw -O L515_31May_1.bag
```

KinectV2
```shell
roslaunch kinect2_bridge kinect2_bridge.launch
rosbag record /kinect2/hd/image_color_rect /kinect2/hd/image_depth_rect -O K2_31May_1.bag
```

D455
```shell
roslaunch realsense2_camera rs_camera.launch
rosbag record camera/color/image_raw camera/depth/image_rect_raw -O D455_31May_1.bag
```

Kinectv4
```shell
roslaunch azure_kinect_ros_driver driver.launch
rosbag record rgb/image_raw depth_to_rgb/image_raw -O K4A_31May_1.bag
```


### Play
```shell
rosbag play -q <bag-files>
```

## Convert Bag to Mp4 using python script

### [Bag to Video (RGB only)](https://github.com/mlaiacker/rosbag2video)
```shell
rosbag2video.py [--fps 25] [--rate 1] [-o outputfile] [-v] [-s] [-t topic] bagfile1 [bagfile2] ...

Converts image sequence(s) in ros bag file(s) to video file(s) with fixed frame rate using ffmpeg
ffmpeg needs to be installed!

--fps   Sets FPS value that is passed to ffmpeg
        Default is 25.
-h      Displays this help.
--ofile (-o) sets output file name.
        If no output file name (-o) is given the filename '<prefix><topic>.mp4' is used and default output codec is h264.
        Multiple image topics are supported only when -o option is _not_ used.
        ffmpeg  will guess the format according to given extension.
        Compressed and raw image messages are supported with mono8 and bgr8/rgb8/bggr8/rggb8 formats.
--rate  (-r) You may slow down or speed up the video.
        Default is 1.0, that keeps the original speed.
-s      Shows each and every image extracted from the rosbag file (cv_bride is needed).
--topic (-t) Only the images from topic "topic" are used for the video output.
-v      Verbose messages are displayed.
--prefix (-p) set a output file name prefix othervise 'bagfile1' is used (if -o is not set).
--start Optional start time in seconds.
--end   Optional end time in seconds.
```
* If your bag file contains both rgb and depth topics, it will just give you warnings and still give you a RGB H.264 video.