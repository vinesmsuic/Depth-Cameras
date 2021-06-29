# Depth Cameras



## To catkin_make with python3 in ROS

```shell
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3
```



```shell
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so
```



## Performance Comparison (Quick view)

* Depth Accuracy: L515 > Kinectv4 > Kinectv2 > D435i > Zed
* Depth Range: Zed > L515 > D455 > KinectV2 > Kinectv4
* RGB resolution: Kinectv4 > All
* FPS: D455 > All
* Price: Max has no clue, Max didn't pay the check




## Current Available Depth Cameras in the Lab:
* [AzureKinect (Kinect V4)](https://docs.microsoft.com/en-us/azure/kinect-dk/hardware-specification)  x 2
* Kinectv2  x 2     - canceled support by Microsoft
* [Realsense D435i](https://www.intelrealsense.com/depth-camera-d435i/) x 0
* [Realsense D455](https://www.intelrealsense.com/depth-camera-d455/) x 1
* [Stereolabs Zed Camera](https://www.stereolabs.com/zed/) x 1
* Realsense LiDAR Camera L515 x 1



## Performance of Each Cameras

> Reference: [Compare Intel cameras](https://www.intelrealsense.com/compare-depth-cameras/)



### L515

* **Full Name:** Intel® RealSense™ LiDAR Camera L515
* **Depth Technology:** LiDAR
* **Depth FOV (H × V):** 70° × 55°
* **Depth Resolution:** Up to 1024 × 768
* **Depth Accuracy Error:** ~5 mm to ~14 mm thru 9m^2
* **Depth Frame Rate:** 30 fps
* **Minimum Depth Distance (Min-Z) at Max Resolution:** ~25 cm
* **Ideal Range:** .25 m to 9 m^3 (Range affected by reflectivity)
* **RGB Frame Rate and Resolution:** 1920 × 1080 at 30 fps
* **RGB Sensor FOV (H × V):** 70° × 43°
* **IMU:** Yes
* **Use Environment:** Indoor only, work in HKSTP inner zone only.



> #### Limitations of L515
>
> [Reference](https://www.intelrealsense.com/optimizing-the-lidar-camera-l515-range/)
>
> L515 depends on signal to noise ratio (SNR), or in other words, the “quality” of the returned signal. Situations that reduce signal quality include ambient light, poor reflective surfaces, laser power, and receiver gain. A change in SNR will have an effect on the final depth result. This section will discuss each of these while giving suggestions on how to optimize for best results.
>
>
> **Ambient Light**
>
> L515 operates at a wavelength of 860nm which is invisible to the human eye and is not affected by common lighting technologies. However, this wavelength is found in sunlight and, therefore, sunlight does have a negative effect on depth quality. When sunlight is present, the camera receiver has difficulty distinguishing between its transmitted laser light code and that of the sunlight. This creates noise leading to low confidence depth or no depth. Because of this, the L515 should only be operated indoors and away from sunlight. Not only direct sunlight, but also sunlight through windows can affect the camera so it is advised not to use the camera near brightly lit windows. Although sunlight is the most common light source containing near IR at 860nm, other light sources that include IR and can reduce L515 performance include halogen and some LED.
>
> HKSTP uses a lot of LED lights, thus L515 only has 2m of range there.
>
> The camera is capable of filtering some ambient sunlight. This can be easily enabled by selecting the “Low Ambient Light” preset in the RealSense SDK or Depth Viewer. The images below show a scene of a table and chairs near a window in an office environment. The quality of the depth in the left image is poor due to the sunlight interfering with the camera. The Low Ambient Light setting is used in the image on the right resulting in a dramatic improvement of depth quality.
>
>
> **Non-optimal Surfaces**
>
> L515 works best on objects that have a reflective and matte surface resulting in a diffuse reflection. If a surface is too smooth and reflective (mirror finish) light hitting the surface at an angle will not reflect back to the camera as illustrated below. Comparatively rough surfaces allow some of the light to be reflected back to the camera and used to calculate distance.
>
> ![](https://www.intelrealsense.com/wp-content/uploads/2020/07/reflections.png)
>
>
> Some material does not reflect much light at all which results in no depth data. An example of such material is darkly colored carpeting and some black plastics. This does not mean that dark carpet cannot be detected by the camera. It does mean that while a wooden floor may produce an excellent depth map at 5 meters distance, the dark carpet may not produce a good depth map until the distance from the camera reduces to 3 or 4 meters.



### D455

* **Full Name:** Intel® RealSense™ Depth Camera D455
* **Depth Technology:** Active IR Stereo
* **Depth FOV (H × V):** 87° × 58°
* **Depth Resolution:** Up to 1280 × 720
* **Depth Accuracy Error:** <2% at 4 m^2
* **Depth Frame Rate:** Up to 90 fps
* **Minimum Depth Distance (Min-Z) at Max Resolution:** ~52 cm
* **Ideal Range:** 0.6 m to 6 m (0.6m to 4m if accuracy concerned)
* **RGB Frame Rate and Resolution:** 1280 × 800 at 30 fps
* **RGB Sensor FOV (H × V):** 90° × 65°
* **IMU:** Yes
* **Use Environment:** Indoor/Outdoor, work in HKSTP



> #### Limitations of D455
> * The depth values are not stable at far range.
> 



### Kinect V2

* **Full Name:** Microsoft Kinect v2 3D-Camera
* **Depth Technology:** Time of Flight (TOF)
* **Depth FOV (H × V):** 70° × 60°
* **Depth Resolution:** 512 x 424
* **Depth Accuracy Error:** -
* **Depth Frame Rate:** 30 fps
* **Minimum Depth Distance (Min-Z) at Max Resolution:** >1m
* **Ideal Range:** 1 to > 4.5m
* **RGB Frame Rate and Resolution:** 1920 x 1080 at 30 fps
* **RGB Sensor FOV (H × V):** 70° × 60°
* **IMU:** No
* **Use Environment:** Indoor/Outdoor, work in HKSTP



> #### Limitations of ToF (Time of Flight) Camera
>
> [Reference](https://www.seeedstudio.com/blog/2020/01/08/what-is-a-time-of-flight-sensor-and-how-does-a-tof-sensor-work/#:~:text=For%20most%20of%20the%20ToF,coherent%20under%20the%20ToF%20sensor.)
>
> **Scattered Light**
>
> In the event where very bright surfaces are located very near your ToF sensor, they can scatter too much light into your receiver and create artefacts and unwanted reflections as your ToF sensor only requires light that has been reflected just once for measurement.
>
> **Multiple Reflections**
>
> When using your ToF sensor on corners and concave shapes, they may cause unwanted reflections as light may be reflected multiple times which distorts measurement.
>
> **Ambient Light**
>
> When using a ToF camera in the great outdoors with bright sunlight can make outdoor use difficult. This is due to the high intensity of the sunlight can cause a quick saturation of the sensor pixels where actual light reflected off an object cannot be detected.






### Kinect V4 / Azure Kinect

* **Full Name:** Microsoft Azure Kinect
* **Depth Technology:** Time of Flight (TOF)
* **Depth FOV (H × V):** up to 120° × 120°
* **Depth Resolution:** up to 1024 × 1024
* **Depth Accuracy Error:** -
* **Depth Frame Rate:**  up to 30 fps, 15 fps if WFOV unbinned
* **Minimum Depth Distance (Min-Z) at Max Resolution:** 0.5m
* **Ideal Range:**  0.5 - 4m
* **RGB Frame Rate and Resolution:**up to 3840 × 2160
* **RGB Sensor FOV (H × V):**  up to 90° × 59°
* **IMU:** Yes
* **Use Environment:** Indoor/Outdoor, work in HKSTP



> #### Limitations of Azure Kinect
>
> first of all It has all the Limitations of ToF (Time of Flight) Camera.
>
> **Unsuitable perating modes**
>
> The depth camera supports the modes indicated below:
>
> [Reference](https://docs.microsoft.com/en-us/azure/kinect-dk/hardware-specification#microphone-array)
>
> | Mode                 | Resolution | Max FPS | Operating Range |
> | -------------------- | ---------- | ------- | --------------- |
> | NFOV unbinned        | 640x576    | 30      | 0.5 - 3.86 m    |
> | NFOV 2x2 binned (SW) | 320x288    | 30      | 0.5 - 5.46 m    |
> | WFOV 2x2 binned      | 512x512    | 30      | 0.25 - 2.88 m   |
> | WFOV unbinned        | 1024x1024  | 15      | 0.25 - 2.21 m   |
> | Passive IR           | 1024x1024  | 30      | N/A             |
>
> **Hardware lag**
>
> It also suffer from lag and latency issues. (25 May 2021)
>
> 



### Zed

* **Full Name:** Stereolabs Zed Camera
* **Depth Technology:** 
* **Depth FOV (H × V):** 
* **Depth Resolution:** 
* **Depth Accuracy Error:** -
* **Depth Frame Rate:** 
* **Minimum Depth Distance (Min-Z) at Max Resolution:** 
* **Ideal Range:** 
* **RGB Frame Rate and Resolution:** 
* **RGB Sensor FOV (H × V):** 
* **IMU:** 
* **Use Environment:** 



> [Questionable ZED accuracy?](https://github.com/stereolabs/zed-examples/issues/44)

