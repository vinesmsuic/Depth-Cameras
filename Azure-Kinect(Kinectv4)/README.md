# To use python3 in ROS
```shell
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3
```

# ROS driver usage - Start the camera node

```shell
roslaunch azure_kinect_ros_driver driver.launch
```

# Azure Kinect

In terms of hardware, Azure Kinect is actually a “bundle” of 4 devices:

- A 4K RGB camera (Color data)
- A wide-angle depth sensor (Depth data)
- An IMU - inertial measurement unit (Accelerometer – Gyroscope)
- A microphone array


### Camera FOV (Field of View)

* The angles that the sensors "see". 
* This diagram shows the RGB camera in a 4:3 mode.

![Camera FOV](https://docs.microsoft.com/en-gb/azure/kinect-dk/media/resources/hardware-specs-media/camera-fov.png)



### Motion sensor (IMU)

* The embedded Inertial Measurement Unit (IMU) is an LSM6DSMUS.
* includes both an accelerometer and a gyroscope.
* The accelerometer and gyroscope are simultaneously sampled at 1.6 kHz. 
* The samples are reported to the host at a 208 Hz.



### Microphone Array

- identifies as a standard USB audio class 2.0 device
- All 7 channels can be accessed.
- Sensitivity: -22 dBFS (94 dB SPL, 1 kHz)
- Signal to noise ratio > 65 dB
- Acoustic overload point: 116 dB

 



# Azure Kinect Development Kit

Azure Kinect DK is a developer kit with advanced AI sensors that provide sophisticated computer vision and speech models. Kinect contains a depth sensor, spatial microphone array with a video camera, and orientation sensor as an all in-one small device with multiple modes, options, and software development kits (SDKs).



### Supported operating systems and architectures

* **Windows 10** April 2018 (Version 1803, OS Build 17134) release (x64) or a later version
* Linux **Ubuntu 18.04** (x64), with a GPU driver that uses OpenGLv4.4 or a later version

