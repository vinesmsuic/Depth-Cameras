##For ref only, directly use docker image instead
##Not done
##TODO automate and turn into a dockerfile
##Do in host if not yet done for mesa swarst
#https://forums.developer.nvidia.com/t/swrast-again/155668/2 not fixed as of jetpack 4.5.1
echo "run manually"
exit
sudo ln -sf /usr/lib/aarch64-linux-gnu/libdrm.so.2.4.0 /usr/lib/aarch64-linux-gnu/libdrm.so.2

# use this as base. If you want nvidia repo, jetson nx = t194
#sudo docker pull mdegans/l4t-base:t194

sudo docker pull nvcr.io/nvidia/l4t-base:r32.5.0
sudo docker tag nvcr.io/nvidia/l4t-base:r32.5.0 robocon_nx
sudo docker run -it --privileged --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix/:/tmp/.X11-unix --volume="$HOME/.Xauthority:/root/.Xauthority:rw" robocon_nx
##Switched to docker instance
apt update -y  && apt install -y dialog nano lsb-release mlocate gnupg && apt upgrade -y
updatedb
##Tzdata (Timezone), set to Asia, Hong Kong
apt install -y tzdata
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

apt update && apt install -y ros-melodic-desktop-full ros-melodic-rgbd-launch git build-essential cmake pkg-config unzip yasm checkinstall libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libavresample-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libxvidcore-dev x264 libx264-dev libfaac-dev libmp3lame-dev libtheora-dev libfaac-dev libmp3lame-dev libvorbis-dev libopencore-amrnb-dev libopencore-amrwb-dev libdc1394-22 libdc1394-22-dev libxine2-dev libv4l-dev v4l-utils libgtk-3-dev python3-dev python3-pip python3-testresources libtbb-dev libatlas-base-dev gfortran libgphoto2-dev libeigen3-dev libhdf5-dev doxygen libgoogle-glog-dev libgflags-dev libprotobuf-dev protobuf-compiler qt5-default ccache libopenblas-dev python3-dev python3-pip python3-setuptools python-pip software-properties-common
cd /usr/include/linux
ln -s -f ../libv4l1-videodev.h videodev.h


echo 'ln -sf /usr/lib/aarch64-linux-gnu/libdrm.so.2.4.0 /usr/lib/aarch64-linux-gnu/libdrm.so.2
' >> ~/.profile
source ~/.bashrc
source '/opt/ros/melodic/setup.bash'



apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential 

rosdep init
rosdep update
 
pip3 install cython flake8 pylint atlas empy
###This will take a very long time (~ 2 hour), may seem to be stuck but it is not (pip is not multi-threaded)
pip3 -vvvvv install numpy pandas pycuda cupy
sudo apt-get install libgtkglext1 libgtkglext1-dev

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


#############################################
apt install -y libssl-dev libusb-1.0-0-dev pkg-config build-essential cmake cmake-curses-gui libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev qtcreator python3 python3-dev apt-utils

export PATH='/usr/local/cuda-10.2/bin:$PATH'
export LD_LIBRARY_PATH='$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64'
export PYTHONPATH="$PYTHONPATH:/usr/local/lib"
/opt/ros/melodic/lib/python2.7/dist-packages:/usr/local/lib:/usr/local/lib/python3.6/pyrealsense2/:/usr/local/lib


#end#
## The above needs to be changed according to cuda version and path##

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
make -j6 && make -j6 install
cp config/99-realsense-libusb.rules /etc/udev/rules.d/

export 'PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2/"' >> ~/.profile
source ~/.bashrc

/opt/ros/melodic/bin:/usr/local/cuda-10.2/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
cd src/

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



curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

apt-add-repository https://packages.microsoft.com/ubuntu/18.04/multiarch/prod

apt update && apt install -y libk4a1.4 libk4a1.4-dev k4a-tools


git clone https://github.com/microsoft/Azure_Kinect_ROS_Driver.git
cd Azure_Kinect_ROS_Driver
git checkout melodic
cd ../

git clone https://github.com/paul-shuvo/iai_kinect2_opencv4.git
cd iai_kinect2_opencv4
git checkout master
cd ../../
-DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so
cd ~
git clone https://github.com/naoki-mizuno/ds4drv --branch devel
cd ds4drv
python3 setup.py install
cp udev/50-ds4drv.rules /etc/udev/rules.d/
udevadm control --reload-rules
udevadm trigger
cd ~/catkin_ws/src
git clone https://github.com/naoki-mizuno/ds4_driver.git
cd ds4_driver
cd ../

catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3

catkin_make install
export PYTHONPATH=/usr/local/lib/python3.6/dist-packages/:/usr/lib/python3.6/dist-packages/:/opt/ros/melodic/lib/python2.7/dist-packages:/opt/ros/melodic/lib/python2.7/dist-packages:/usr/local/lib:/usr/local/lib/python3.6/pyrealsense2/

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc


sudo pip3 install rospkg 
sudo pip3 install netifaces
sudo pip3 install defusedxml

apt install -y bluez bluetooth
##https://stackoverflow.com/questions/28868393/accessing-bluetooth-dongle-from-inside-docker

####Dont forget to commit your changes in docker before exiting