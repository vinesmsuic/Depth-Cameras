cd ~
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense/
git checkout $LIBREALSENSE_VERSION
mkdir build
cd build
/usr/bin/cmake ../ -DBUILD_EXAMPLES=true -DFORCE_LIBUVC=true -DBUILD_WITH_CUDA="true" -DCMAKE_BUILD_TYPE=release -DBUILD_PYTHON_BINDINGS=bool:true
sudo make install
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
