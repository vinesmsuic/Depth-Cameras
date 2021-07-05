
# Installations

## Install ROS Melodic If you haven't

### on Computers
See [http://wiki.ros.org/melodic/Installation](http://wiki.ros.org/melodic/Installation).

### on Nvidia Jetson
See [https://github.com/jetsonhacks/installROS](https://github.com/jetsonhacks/installROS).

```shell
./installROS.sh -p ros-melodic-desktop-full -p ros-melodic-rgbd-launch
```

## Install Jet-Pack (Nvidia Jetson only) If you haven't

```shell
sudo apt update
sudo apt install nvidia-jetpack
```

## Install OpenCV with CUDA acceleration

```shell
cd ~
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout tags/4.5.2
cd ..
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout tags/4.5.2
mkdir build
cd build

##Change according to cuda/gcc version
cmake --clean-first \
-D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
-D WITH_OPENCL=ON \
-D WITH_CUDA=ON \
-D CUDA_ARCH_BIN=7.2 \
-D WITH_CUDNN=ON \
-D CUDNN_VERSION='8.0' \
-D WITH_CUBLAS=ON \
-D ENABLE_FAST_MATH=ON \
-D CUDA_FAST_MATH=ON \
-D OPENCV_DNN_CUDA=ON \
-D ENABLE_NEON=ON \
-D BUILD_opencv_cudacodec=ON \
-D WITH_QT=OFF \
-D WITH_OPENMP=ON \
-D WITH_OPENGL=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_GSTREAMER=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=ON \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_opencv_python3=TRUE \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D WITH_NVCUVID=ON\
-D BUILD_EXAMPLES=ON ..

########### make will take ~ 2 hours, also make sure ram is not occupied 

make -j6 && make -j6 install
```



### On Nvidia Jetson TX1, TX2

See [https://github.com/jetsonhacks?tab=repositories&q=OpenCV&type=&language=&sort=](https://github.com/jetsonhacks?tab=repositories&q=OpenCV&type=&language=&sort=) and find the corrsponding repo.

## Install K4A SDK and K4A ROS wrapper

### For Azure Kinect 
See [Here the setup guide of K4A (PC only)](https://github.com/PolyU-Robocon/Depth-Cameras/blob/main/Azure-Kinect(Kinectv4)/SETUP.md)
For Jetson and other ARM architecture, go google yourself

## Install KinectV2 SDK and K2 ROS wrapper

### For Kinect V2
See [Here the setup guide of K2](https://github.com/PolyU-Robocon/Depth-Cameras/blob/main/Kinectv2/SETUP.md)


## Install Intel RealSense SDK and Realsense ROS wrapper

If you are using D435/D455/L515, you need Intel RealSense SDK.

### Install Intel RealSense SDK

Intel RealSense update insanely quick so I would not recommend using a script to install it. 

#### on Linux Computers
See [https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)



#### on Nvidia Jetson

Install Jetpack

```shell
sudo apt update
###Dont install nvidia-jetpack in a docker container###
sudo apt install nvidia-jetpack
```

Get dependencies if you don't have yet

```shell
apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential 

rosdep init
rosdep update
 
pip3 install cython flake8 pylint atlas empy
###This will take a very long time (~ 2 hour), may seem to be stuck but it is not (pip is not multi-threaded)
pip3 -vvvvv install numpy pandas pycuda cupy
sudo apt-get install libgtkglext1 libgtkglext1-dev
```

build Install OpenCV (GPU version)

```shell

cd ~
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout tags/4.5.2
cd ..
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout tags/4.5.2
mkdir build
cd build

##Change according to cuda/gcc version
cmake --clean-first \
-D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
-D WITH_OPENCL=ON \
-D WITH_CUDA=ON \
-D CUDA_ARCH_BIN=7.2 \
-D WITH_CUDNN=ON \
-D CUDNN_VERSION='8.0' \
-D WITH_CUBLAS=ON \
-D ENABLE_FAST_MATH=ON \
-D CUDA_FAST_MATH=ON \
-D OPENCV_DNN_CUDA=ON \
-D ENABLE_NEON=ON \
-D BUILD_opencv_cudacodec=ON \
-D WITH_QT=ON \
-D WITH_OPENMP=ON \
-D WITH_OPENGL=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_GSTREAMER=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=ON \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_opencv_python2=ON \
-D BUILD_opencv_python3=ON \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D WITH_NVCUVID=ON\
-D BUILD_EXAMPLES=ON ..

########### make will take ~ 2 hours, also make sure ram is not occupied 

make -j6 && make -j6 install
```

Config paths

```shell
#############################################
apt install -y libssl-dev libusb-1.0-0-dev pkg-config build-essential cmake cmake-curses-gui libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev qtcreator python3 python3-dev apt-utils

export PATH='/usr/local/cuda-10.2/bin:$PATH'
export LD_LIBRARY_PATH='$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64'
export PYTHONPATH="$PYTHONPATH:/usr/local/lib"
/opt/ros/melodic/lib/python2.7/dist-packages:/usr/local/lib:/usr/local/lib/python3.6/pyrealsense2/:/usr/local/lib


#end#
## The above needs to be changed according to cuda version and path##
```

Download RealSense SDK and build

```shell
cd ~
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense/
git checkout v2.45.0


##kernel patch, see https://github.com/IntelRealSense/librealsense/blob/v2.45.0/doc/installation_jetson.md##
#########Only do this on the host nx, do not run the script in the docker instance#########
./scripts/patch-realsense-ubuntu-L4T.sh  
####################################################################################

./scripts/setup_udev_rules.sh  

mkdir build
cd build

/usr/bin/cmake ../ -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DBUILD_PYTHON_BINDINGS=bool:true -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true
sudo make -j6 && sudo make install
cp config/99-realsense-libusb.rules /etc/udev/rules.d/

##add the pyrealsense lib path, change accordingly to python version##
export 'PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2/"' >> ~/.profile
source ~/.bashrc
```

Reboot the Jetson

Finally set up ROS environment

```shell
##after reboot the jetson nx#
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
cd src/

# See Install Intel RealSense ROS Wrapper part
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout 2.3.0
cd ../

git clone https://github.com/pal-robotics/ddynamic_reconfigure.git
cd ddynamic_reconfigure/
git checkout 0.4.1
cd ../


git clone https://github.com/MartinNievas/vision_opencv.git
cd vision_opencv/
git checkout compile_oCV4
cd ../


catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release

catkin_make install
export PYTHONPATH=/usr/local/lib/python3.6/dist-packages/:/usr/lib/python3.6/dist-packages/:/opt/ros/melodic/lib/python2.7/dist-packages:/opt/ros/melodic/lib/python2.7/dist-packages:/usr/local/lib:/usr/local/lib/python3.6/pyrealsense2/

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```



### Install Intel RealSense ROS Wrapper

You need:
* ROS
* RealSense SDK

MAKE SURE THE ROS Wrapper Match the version of RealSense SDK.
otherwise you might encounter this error:
[RealSense SDK 2.0 is not detected in realsense-ros/realsense2_camera even it is installed](https://github.com/IntelRealSense/realsense-ros/issues/1322)

* You can check the version here. [https://github.com/IntelRealSense/realsense-ros/tags](https://github.com/IntelRealSense/realsense-ros/tags)

Create a catkin workspace if you haven't
```shell
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
```


Specifically, make sure that the ros package `ddynamic_reconfigure` is installed. If you haven't install it through APT:

```shell
git clone https://github.com/pal-robotics/ddynamic_reconfigure.git
```

Get ros package Realsense ROS
```shell
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/

#We use 2.21 for LibRealSense SDK v2.41.0
git checkout 2.2.21

#Instead of
#git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`


cd ..
```

```shell
catkin_init_workspace
cd ..
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install
```

If you haven't put it into source
```shell
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```


[More info of RealSense ROS Wrapper](https://github.com/IntelRealSense/realsense-ros)


### Python Wrapper of Realsense

The pyrealsense2 package is a official wrapper which does support RealSense SDK 2.0.

Get pip3 if you don't have it yet
```shell
sudo apt install python3-pip
```

#### Linux PC environment
For PC environment
```shell
pip3 install pyrealsense2
```

#### Jetson and other ARM architecture
For Jetson and other ARM architecture, you need to get the whl file.
Get it from here: [https://pypi.org/project/pyrealsense2-aarch64/#files](https://pypi.org/project/pyrealsense2-aarch64/#files)
Then:

```shell
pip3 install ~/Downloads/pyrealsense2_aarch64-2.23.0-cp36-none-any.whl 
```

