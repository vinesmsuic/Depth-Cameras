## Setup of Azure Kinect DK (Ubuntu 18.04)

Remember to stictly follow `sudo` command otherwise the command will produce errors.

### Sensor SDK - via source

Make sure your linux is AMD64.

```shell
dpkg --print-architecture
```

> For ARM64, the setup is a bit different so please refer to offical document.



You need to have cmake version >3.9

```shell
git clone https://github.com/microsoft/Azure-Kinect-Sensor-SDK.git
cd Azure-Kinect-Sensor-SDK
mkdir build && cd build
cmake .. -GNinja
ninja
sudo ninja install
```

> [You might encounter ninja: error: 'LIBSOUNDIO_LIB-NOTFOUND', needed by 'bin/k4aviewer', missing and no known rule to make it](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/405)
>
> Solve it by installing the leftover dependency and `cmake .. -GNinja` again. Then `ninja` and `ninja install`.
>


Depth Engine Not Found?
> The depth engine is closed source and comes with the apt package and is not included in this repo. The depth engine (DE) is a closed source binary shipped with the Linux Debian package. As an example, run `apt install libk4a1.3` to install the Azure Kinect 1.3 and get the depth engine. See using the depth engine for information about versioning and adding the Microsoft's Package Repository to your machine. NOTE This step is not need for building, but is required running the SDK.

To get Depth Engine:
Firstly, configure Microsoft's Package Repository

```shell
curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
```

If you are using ARM, replace `https://packages.microsoft.com/ubuntu/18.04/prod` with `https://packages.microsoft.com/ubuntu/18.04/multiarch/prod`.
```shell
sudo apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod
```

```shell
sudo apt-get update
```



```shell
sudo apt install libk4a1.3
sudo apt install libk4a1.3-dev
```




### Invoke k4aviewer in bin

Before writing a test program, lets check if we setup correctly.

To see if we setup correctly , start the [Azure Kinect Viewer](https://docs.microsoft.com/en-gb/azure/kinect-dk/azure-kinect-viewer)

```shell
whereis k4aviewer
sudo k4aviewer
```



### Invoke k4aviewer without Root

On Linux, once attached, the device should automatically enumerate and load all drivers. However, in order to use the Azure Kinect SDK with the device and without being 'root', you will need to setup udev rules. We have these rules checked into this repo under 'scripts/99-k4a.rules'. 

To do so: 

* Copy 'scripts/99-k4a.rules' into '/etc/udev/rules.d/'. 
* Detach and reattach Azure Kinect devices if attached during this process. 

```shell
cd /etc/udev/rules.d/
sudo vi 99-k4a.rules
```



`99-k4a.rules` File:

```
# Bus 002 Device 116: ID 045e:097a Microsoft Corp.  - Generic Superspeed USB Hub
# Bus 001 Device 015: ID 045e:097b Microsoft Corp.  - Generic USB Hub
# Bus 002 Device 118: ID 045e:097c Microsoft Corp.  - Azure Kinect Depth Camera
# Bus 002 Device 117: ID 045e:097d Microsoft Corp.  - Azure Kinect 4K Camera
# Bus 001 Device 016: ID 045e:097e Microsoft Corp.  - Azure Kinect Microphone Array

BUS!="usb", ACTION!="add", SUBSYSTEM!=="usb_device", GOTO="k4a_logic_rules_end"

ATTRS{idVendor}=="045e", ATTRS{idProduct}=="097a", MODE="0666", GROUP="plugdev"
ATTRS{idVendor}=="045e", ATTRS{idProduct}=="097b", MODE="0666", GROUP="plugdev"
ATTRS{idVendor}=="045e", ATTRS{idProduct}=="097c", MODE="0666", GROUP="plugdev"
ATTRS{idVendor}=="045e", ATTRS{idProduct}=="097d", MODE="0666", GROUP="plugdev"
ATTRS{idVendor}=="045e", ATTRS{idProduct}=="097e", MODE="0666", GROUP="plugdev"

LABEL="k4a_logic_rules_end"
```

Once complete, the Azure Kinect camera is available without being 'root' or 'sudo'.

```shell
k4aviewer
```

> YOU MUST DO THIS STEP IN ORDER TO USE WITH ROS.


## Update Firmware of Azure Kinect DK

We might want to update our firmware.



List connected devices

```shell
sudo AzureKinectFirmwareTool -l
```

Then the shell should print something like this:

```shell
== Azure Kinect DK Firmware Tool ==
Found 2 connected devices:
0: Device "000036590812"
1: Device "000274185112"
```



check device firmware version

```shell
sudo AzureKinectFirmwareTool -q
```

Then the shell should print something like this:

```shell
== Azure Kinect DK Firmware Tool ==
Device Serial Number: 000036590812
Current Firmware Versions:
    RGB camera firmware:      1.5.92
    Depth camera firmware:    1.5.66
    Depth config file:        6109.7
    Audio firmware:           1.5.14
    Build Config:             Production
    Certificate Type:         Microsoft
```



Now get [the Latest Firmware here(Pinned Issue)](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues)

Lets say you downloaded the firmware bin file into `Downloads` folder:

Inspect the firmware

```shell
sudo AzureKinectFirmwareTool -i Downloads/AzureKinectDK_Fw_1.6.110079014.bin
```

Update device firmware

```shell
sudo AzureKinectFirmwareTool -u Downloads/AzureKinectDK_Fw_1.6.110079014.bin 
```



# Sidenote

> Actually, it is better to use a [Dockerfile](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/scripts/docker/Dockerfile) to ensure your machine has required dependencies.
>
> https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/docs/building.md



### Install Sensor SDK - via apt

Besides getting it via source, you can also install it from apt.

Firstly, configure Microsoft's Package Repository

```shell
curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
```

If you are using ARM, replace `https://packages.microsoft.com/ubuntu/18.04/prod` with `https://packages.microsoft.com/ubuntu/18.04/multiarch/prod`.
```shell
sudo apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod
```

```shell
sudo apt-get update
```



Then We can install the necessary packages.

```shell
sudo apt install k4a-tools
```

> It will automatically downloads the latest version of `libk4a1.X` as well.





### Don't install Sensor SDK via both apt and source

> In case you built the k4a-tools through both apt and source, you may probably encounter problem (since you have 2 k4a-tools in your system) and you need to delete one of them.
>
> https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/1453



# Azure Kinect ROS Driver



## Pre-requisites

[Read this](https://github.com/microsoft/Azure_Kinect_ROS_Driver/blob/melodic/docs/building.md)

* Get ROS Melodic for Ubuntu 18.04
* Get Azure Kinect Sensor SDK



> Optional : Inital your workspace
>
> ```shell
> mkdir -p ~/AzureKinect_ws/src
> cd ~/AzureKinect_ws/src
> catkin_init_workspace
> ```



Go to `catkin_ws/src` or src of your ws folder (the ws folder in Optional part)

```shell
git clone https://github.com/microsoft/Azure_Kinect_ROS_Driver.git
```



## Test Azure Kinect ROS Driver with rviz

```shell
cd catkin_ws
catkin_make
catkin_make install
```



```shell
source ./devel/setup.bash
roslaunch azure_kinect_ros_driver driver.launch
```



### Verifying the Camera is connected - Way1

Open another terminal to run rviz.

```shell
rviz
```

> Click Add->Image->Image Topic->/rgb/image_raw
>
> Click Add->Image->Image Topic->/depth_to_rgb/image_raw

You should see the camera.

![](https://i.imgur.com/GnxMDeK.png)

![](https://i.imgur.com/Yzoevhc.png)



Open another terminal to start the rqt_graph

```shell
rosrun rqt_graph rqt_graph
```

Click Nodes/Topics(active) and refresh the page

You should see something like this:

![](https://i.imgur.com/OGP1C4r.png)





###  Verifying the Camera is connected - Way2

Another way to check the camera.



Open another terminal to run:

```shell
rosrun rqt_gui rqt_gui
```

Click Plugins -> Visualization -> Image View

Then select /rgb/image_raw and refresh the page.

You should see something like this.

![](https://i.imgur.com/YuEOPGu.png)



Open another terminal to start the rqt_graph

```shell
rosrun rqt_graph rqt_graph
```

Click Nodes/Topics(active) and refresh the page

You should see something like this:

![](https://i.imgur.com/1rDeb8j.png)





### Finally

Check active topic

```shell
rostopic list
```

Check active topic (detailed)

```she
rostopic list -v
```





> * If you want to record the topic using `rosbag`
>   * `rosbag record -O image.bag /rgb/image_raw /depth_to_rgb/image_raw`
> * If you want to playback the rosbag
>   * `rosbag play image.bag`



Now you can use ros topic to collect the depth and rgb from the kinect.



# Reference

* [Azure Kinect DK documentation on Github(READ THIS FIRST)](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/tree/develop/docs)
* [Azure Kinect DK documentation](https://docs.microsoft.com/en-gb/azure/kinect-dk/)
* [Notes on Setting up the Microsoft Azure Kinect on Ubuntu 18.04](https://gist.github.com/madelinegannon/c212dbf24fc42c1f36776342754d81bc)


* https://github.com/microsoft/Azure_Kinect_ROS_Driver/blob/melodic/docs/building.md
* https://blog.csdn.net/qq_27399933/article/details/107356117
* https://blog.csdn.net/zxxxiazai/article/details/108152376
