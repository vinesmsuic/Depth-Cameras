# Setup-Zed-camera

### Step

* #### Download Zed SDK
* #### Update or Install CUDA (optional)
* #### Download zed_ros_wrapper

### Download Zed SDK

#### According to https://www.stereolabs.com/developers/release/ to find out which is suitable for your OS
##### It will also show what CUDA version that Zed camera required
##### find out where is Zed SDK file after download
##### If it is zip files, just extract it 
##### If not please access to the command line with Zed SDK directory, then type the following code

```XML
chmod +x ZED_SDK_Linux_*.run
./ZED_SDK_Linux_*.run
```
# If ZED SDK said that want to update your CUDA version automatically, don't type yes otherwise your may not able to open ubuntu system anymore 
#### The best way is to check your current CUDA version in command line first.

```XML
nvcc --version

nvcc: NVIDIA (R) Cuda compiler driver
...
Build cuda_xx.0_bu.TC445_37.28845127_0
```
#### Build cuda_xx.0_bu show your current cuda version

### Update or Install CUDA (optional)

#### Look at the guideline for this https://vinesmsuic.github.io/2021/01/10/linux-cuda/#do-this-if-you-already-have-cuda-and-you-want-to-downgrade-it

### Download zed_ros_wrapper

##### Type the following code in command line

```XML
$ cd ~/catkin_ws/src
$ git clone https://github.com/stereolabs/zed-ros-wrapper.git
$ cd ../
$ rosdep install --from-paths src --ignore-src -r -y
$ catkin_make -DCMAKE_BUILD_TYPE=Release
$ source ./devel/setup.bash
```
##### After download the zed_ros_wrapper, you can open the Zed camera in ROS

##### Connect Zed camera to USB port and launch the ZED node before using any services
```XML
$ roslaunch zed_wrapper zed.launch
```

##### If you want to see the camera window, please open rviz (type following code)

```XML
rosrun rviz rviz
```
##### Then subscribe Zed camera node in RVIZ
