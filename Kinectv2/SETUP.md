# Setup of Kinect V2 SDK (libfreenect2)

```shell
git clone https://github.com/OpenKinect/libfreenect2.git
```

## first get dependencies

```shell
sudo apt-get install build-essential cmake pkg-config libturbojpeg libjpeg-turbo8-dev mesa-common-dev freeglut3-dev libxrandr-dev libxi-dev 
```

```shell
sudo apt-get install libglfw3-dev
sudo apt-get install libopenni2-dev
sudo apt-get install libusb-1.0-0-dev
sudo apt-get install libturbojpeg0-dev
```

> If you can't get `sudo apt-get install libusb-1.0-0-dev`, try:
```shell
sudo apt-add-repository ppa:floe/libusb
sudo apt-get update
sudo apt-get install libusb-1.0-0-dev
```

## start building

Go to the path we cloned to

```shell
cd libfreenect2
mkdir build 
cd build
cmake ..
make
sudo make install
```

## set udev rules

Go to the path of your libfreenect2 folder
```shell
sudo cp libfreenect2/platform/linux/udev/90-kinect2.rules /etc/udev/rules.d/
```

Replug the Kinect2 and run in build folder:
```shell
./bin/Protonect
```


# Setup of Kinect V2 ROS Driver

First go to your ROS workspace src folder (`catkin_ws` for example)
```shell
cd ~/catkin_ws/src/
```

## Installing iai_kinect2

**Note: If you are using OpenCV version => 4, install the special version of iai_kinect2.**
> If you are using Jetson Xavier NX, you are probably using OpenCV version => 4.
```shell
git clone https://github.com/paul-shuvo/iai_kinect2_opencv4.git
cd iai_kinect2_opencv4
rosdep install -r --from-paths .
```

If you are using OpenCV version <4 :

```shell
git clone https://github.com/code-iai/iai_kinect2.git
cd iai_kinect2
rosdep install -r --from-paths .
```

## Build and Run

```shell
cd ~/catkin_ws
catkin_make -DCMAKE_BUILD_TYPE="Release"
```

> 
> Troubleshooting
> 
> For any problem related to `opencv` not found, create a symbolic link between the 2 opencv folders.
> ```
> sudo ln -s /usr/include/opencv4/opencv2/ /usr/include/opencv
> ```
> 
> For any problem related to `recipe for target 'iai_kinect2/kinect2_bridge/CMakeFiles/kinect2_bridge_nodelet.dir/all' failed, needed by xxxxx. Stop.`
> ```
> sudo apt install libopencv3.2
> ```
> 

```shell
source ~/catkin_ws/devel/setup.bash
```

Open 2 terminals
```shell
roslaunch kinect2_bridge kinect2_bridge.launch
```

Available ROS Topics:
HD Topics
The images in this topics have a FullHD resolution (1920x1080).

Note: For correct registration of the depth image to the color image it is needed to perform a calibration.
HD (RGB + Depth): `/kinect2/hd/image_color` + `/kinect2/hd/image_depth_rect`


```shell
rosrun kinect2_viewer kinect2_viewer
```



# Reference

https://blog.csdn.net/boyhoodme/article/details/89059888
