# Depth-Cameras


## Performance Comparison (Quick view)

* Compatibility: Kinectv2 > D435i > Zed > Kinectv4
* Depth Accuracy: Kinectv4 > Kinectv2 > D435i > Zed
* Depth Range:
* RGB resolution:
* FPS:
* Price: 




## Current Available Depth Cameras in the Lab:
* [AzureKinect (Kinect V4)](https://docs.microsoft.com/en-us/azure/kinect-dk/hardware-specification)  x 2
* Kinectv2  x 2     - canceled support by Microsoft
* [Realsense D435i](https://www.intelrealsense.com/depth-camera-d435i/) x 0
* [Stereolabs Zed Camera](https://www.stereolabs.com/zed/) x 1
* Realsense LiDAR Camera L515 x 1


## Common Mistakes

* To use the script, you need to set it executable.

```shell
sudo chmod +x yourfile.py
```

* Use USB 3.0 Port instead of 2.0 .

## Install Intel RealSense SDK and Correct Realsense ROS wrapper (If you are using D435/D455/L515)

If you are using D435/D455/L515, you need Intel RealSense SDK to make

### Install Intel RealSense SDK

Here is a script to build realsenseSDK on the Nvidia JetsonNX (Should also work in PC / Laptop environment)

```shell
sudo ./build_realsenseSDK.sh
```

Verify Installation
```shell
realsense-viewer
```

### Install Intel RealSense ROS Wrapper

You need:
* ROS
* RealSense SDK

MAKE SURE THE ROS Wrapper Match the version of RealSense SDK.
otherwise you might encounter this error:
[RealSense SDK 2.0 is not detected in realsense-ros/realsense2_camera even it is installed](https://github.com/IntelRealSense/realsense-ros/issues/1322)


Create a catkin workspace if you haven't
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
```

```
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/

#We use 

#Instead of
#git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`


cd ..
```

