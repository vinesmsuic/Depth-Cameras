sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
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
echo 'export PATH="/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"' >> ~/.profile
source ~/.profile

cd ~
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense/
git checkout $LIBREALSENSE_VERSION
mkdir build
cd build
/usr/bin/cmake ../ -DBUILD_EXAMPLES=true -DFORCE_LIBUVC=true -DBUILD_WITH_CUDA="true" -DCMAKE_BUILD_TYPE=release -DBUILD_PYTHON_BINDINGS=bool:true
sudo make install
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
