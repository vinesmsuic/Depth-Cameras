##For jetson nx only##
echo "run manually"

exit
sudo apt update
##Confirmation prompts may pop up##
###Dont install nvidia-jetpack in a docker container###
sudo apt install nvidia-jetpack
###
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update && sudo apt install -y ros-melodic-desktop-full ros-melodic-rgbd-launch
echo "source '/opt/ros/melodic/setup.bash'" >> ~/.bashrc
source ~/.bashrc
sudo apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init
rosdep update
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo bionic main" -u
sudo apt update
sudo apt upgrade -y
sudo apt install -y libssl-dev libusb-1.0-0-dev pkg-config build-essential cmake cmake-curses-gui libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev qtcreator python3 python3-dev apt-utils nano mlocate
updatedb
##https://forums.developer.nvidia.com/t/swrast-again/155668/2 not fixed as of jetpack 4.5.1
sudo ln -sf /usr/lib/aarch64-linux-gnu/libdrm.so.2.4.0 /usr/lib/aarch64-linux-gnu/libdrm.so.2

## The following needs to be copied and pasted, do not run each line seperatly#
echo 'export PATH="/usr/local/cuda-10.2/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64"
export PYTHONPATH="$PYTHONPATH:/usr/local/lib"' >> ~/.profile
source ~/.bashrc
#end#
## The above needs to be changed according to cuda version and path##


cd ~
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense/
git checkout v2.45.0
##kernel patch, see https://github.com/IntelRealSense/librealsense/blob/v2.45.0/doc/installation_jetson.md##
./scripts/patch-realsense-ubuntu-L4T.sh  

##reboot the jetson nx##
sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev -y
./scripts/setup_udev_rules.sh  

mkdir build
cd build
##the default should be python 3.6 if it is installed and configured in update-alternatives#
# or else 
# If you have multiple python installations on your machine you can use: -DPYTHON_EXECUTABLE=<path to python executable>
#Instead of cmake, you can use cmake-gui for gui assisted configurations
/usr/bin/cmake ../ -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DBUILD_PYTHON_BINDINGS=bool:true -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true

###Not used###
#sudo uninstall
#sudo make clean
###end#######

sudo make -j6 && sudo make install
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/

##add the pyrealsense lib path, change accordingly to python version##
export 'PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2/"' >> ~/.profile
source ~/.bashrc


##reboot the jetson nx#
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
cd ../../



###Not used###
#catkin_make clean
###end#######

catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DOpenCV_DIR='/usr/lib/aarch64-linux-gnu/cmake/opencv4/'
catkin_make install

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

##### COPY the .so files to your .py folder if directly importing pyrealsense2 does not work###
cd /usr/local/lib/python3.6/pyrealsense2/

###roslaunch realsense2_camera rs_camera.launch enable_infra:=true align_depth:=true initial_reset:=true enable_sync:=true
###need to set to compressed due to bandwidth limitations##
###https://github.com/IntelRealSense/realsense-ros/issues/1510#issuecomment-839616982###
###https://user-images.githubusercontent.com/73002545/117951760-c32a9e00-b314-11eb-878b-121f5e513184.png###






