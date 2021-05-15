echo "run manually"
exit
sudo apt update
##May have manual pop up##
sudo apt install nvidia-jetpack
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
sudo apt install ros-melodic-rgbd-launch
source '/opt/ros/melodic/setup.bash' >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init
rosdep update
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo bionic main" -u
sudo apt update
sudo apt upgrade -y
sudo apt install -y libssl-dev libusb-1.0-0-dev pkg-config build-essential cmake cmake-curses-gui libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev qtcreator python3 python3-dev apt-utils librealsense2-utils librealsense2-dev

echo 'export PATH="/usr/local/cuda-10.2/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda-10.2/lib64"
export PYTHONPATH="$PYTHONPATH:/usr/local/lib"' >> ~/.profile
source ~/.bashrc

cd ~
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense/
git checkout v2.45.0
##kernel patch https://github.com/IntelRealSense/librealsense/blob/v2.45.0/doc/installation_jetson.md##
./scripts/patch-realsense-ubuntu-L4T.sh  

##reboot##
sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev -y
./scripts/setup_udev_rules.sh  
export 'PYTHONPATH="$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2/"' >> ~/.profile
source ~/.bashrc

mkdir build
cd build
##defualt should use python 3.6 if installed and configured in update alternatives#
/usr/bin/cmake ../ -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DBUILD_PYTHON_BINDINGS=bool:true -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true && make -j$(($(nproc)-1)) && sudo make install 

sudo make uninstall && sudo make clean && sudo make -j5 && sudo make install
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/



# reboot
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/

git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout 2.3.0
cd ..
sudo apt install ros-melodic-ddynamic-reconfigure
##IMPORTANT MANUAL#############
echo "READ SCRIPT"
nano /opt/ros/melodic/share/cv_bridge/cmake/cv_bridgeConfig.cmake
##replace all instances /usr/include/opencv with /usr/include/opencv4
## Nvidia precompiled opencv4##

catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

##### COPY the .so files to your .py folder if directly importing does not work so that pyrealsense2 can be imported###
cd /usr/local/lib/python3.6/pyrealsense2/