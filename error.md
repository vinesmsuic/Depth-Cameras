robocon@robocon-desktop:~/catkin_ws$ catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so
Base path: /home/robocon/catkin_ws
Source space: /home/robocon/catkin_ws/src
Build space: /home/robocon/catkin_ws/build
Devel space: /home/robocon/catkin_ws/devel
Install space: /home/robocon/catkin_ws/install
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
####
#### Running command: "cmake /home/robocon/catkin_ws/src -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so -DCATKIN_DEVEL_PREFIX=/home/robocon/catkin_ws/devel -DCMAKE_INSTALL_PREFIX=/home/robocon/catkin_ws/install -G Unix Makefiles" in "/home/robocon/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/robocon/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /home/robocon/k2_ws/devel;/home/robocon/catkin_ws/devel;/opt/ros/melodic
-- This workspace overlays: /home/robocon/k2_ws/devel;/home/robocon/catkin_ws/devel;/opt/ros/melodic
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.6.9", minimum required is "2") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python3
-- Using Debian Python package layout
-- Using empy: /usr/bin/empy
-- Using CATKIN_ENABLE_TESTING: False
-- catkin 0.7.29
-- BUILD_SHARED_LIBS is on
-- Found OpenCV: /usr/local (found suitable version "4.5.2", minimum required is "4.5.1") 
CMake Warning at /usr/share/cmake-3.10/Modules/FindBoost.cmake:1626 (message):
  No header defined for python3; skipping header check
Call Stack (most recent call first):
  CMakeLists.txt:71 (find_package)


-- Boost version: 1.65.1
-- Found the following Boost libraries:
--   python3
-- BUILD_SHARED_LIBS is on
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 22 packages in topological order:
-- ~~  - iai_kinect2 (metapackage)
-- ~~  - opencv_tests
-- ~~  - realsense2_description
-- ~~  - vision_opencv (metapackage)
-- ~~  - shooterControll
-- ~~  - cv_bridge
-- ~~  - ds4_driver
-- ~~  - image_geometry
-- ~~  - depth_detector_py
-- ~~  - kinect2_registration
-- ~~  - rs-ros-scripts
-- ~~  - robot_gui_bridge
-- ~~  - temp_scripts
-- ~~  - kinect2_bridge
-- ~~  - kinect2_calibration
-- ~~  - kinect2_viewer
-- ~~  - realsense2_camera
-- ~~  - UT395B
-- ~~  - usb_cam
-- ~~  - mobile_robot_2dnav
-- ~~  - azure_kinect_ros_driver
-- ~~  - xbox_node
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin metapackage: 'iai_kinect2'
-- ==> add_subdirectory(iai_kinect2_opencv4/iai_kinect2)
-- +++ processing catkin package: 'opencv_tests'
-- ==> add_subdirectory(vision_opencv/opencv_tests)
-- +++ processing catkin package: 'realsense2_description'
-- ==> add_subdirectory(realsense-ros/realsense2_description)
-- +++ processing catkin metapackage: 'vision_opencv'
-- ==> add_subdirectory(vision_opencv/vision_opencv)
-- +++ processing catkin package: 'shooterControll'
-- ==> add_subdirectory(shooterControll)
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
-- +++ processing catkin package: 'cv_bridge'
-- ==> add_subdirectory(vision_opencv/cv_bridge)
-- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython3.6m.so (found version "3.6.9") 
CMake Warning at /usr/share/cmake-3.10/Modules/FindBoost.cmake:1626 (message):
  No header defined for python3; skipping header check
Call Stack (most recent call first):
  vision_opencv/cv_bridge/CMakeLists.txt:11 (find_package)


-- Boost version: 1.65.1
-- Found the following Boost libraries:
--   python3
-- Found OpenCV: /usr/local (found version "4.5.2") found components:  opencv_core opencv_imgproc opencv_imgcodecs 
-- Found PythonInterp: /usr/bin/python3 (found version "3.6.9") 
-- Found PythonLibs: /usr/lib/aarch64-linux-gnu/libpython3.6m.so (found suitable version "3.6.9", minimum required is "3.6") 
-- +++ processing catkin package: 'ds4_driver'
-- ==> add_subdirectory(ds4_driver)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- ds4_driver: 4 messages, 0 services
-- +++ processing catkin package: 'image_geometry'
-- ==> add_subdirectory(vision_opencv/image_geometry)
-- Found OpenCV: /usr/local (found version "4.5.2") 
-- +++ processing catkin package: 'depth_detector_py'
-- ==> add_subdirectory(depth_detector_py)
-- +++ processing catkin package: 'kinect2_registration'
-- ==> add_subdirectory(iai_kinect2_opencv4/kinect2_registration)
-- CPU based depth registration enabled
-- OpenCL based depth registration enabled
CMake Warning at iai_kinect2_opencv4/kinect2_registration/CMakeLists.txt:60 (message):
  Your libOpenCL.so is incompatible with CL/cl.h.  Install ocl-icd-opencl-dev
  to update libOpenCL.so?


-- +++ processing catkin package: 'rs-ros-scripts'
-- ==> add_subdirectory(rs-ros-scripts)
-- +++ processing catkin package: 'robot_gui_bridge'
-- ==> add_subdirectory(robot_gui_bridge)
-- +++ processing catkin package: 'temp_scripts'
-- ==> add_subdirectory(temp_scripts)
-- +++ processing catkin package: 'kinect2_bridge'
-- ==> add_subdirectory(iai_kinect2_opencv4/kinect2_bridge)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- +++ processing catkin package: 'kinect2_calibration'
-- ==> add_subdirectory(iai_kinect2_opencv4/kinect2_calibration)
-- +++ processing catkin package: 'kinect2_viewer'
-- ==> add_subdirectory(iai_kinect2_opencv4/kinect2_viewer)
-- Boost version: 1.65.1
-- Found the following Boost libraries:
--   system
--   filesystem
--   thread
--   date_time
--   iostreams
--   serialization
--   chrono
--   atomic
--   regex
-- Could NOT find ensenso (missing: ENSENSO_LIBRARY ENSENSO_INCLUDE_DIR) 
** WARNING ** io features related to ensenso will be disabled
-- Could NOT find DAVIDSDK (missing: DAVIDSDK_LIBRARY DAVIDSDK_INCLUDE_DIR) 
** WARNING ** io features related to davidSDK will be disabled
-- Could NOT find DSSDK (missing: _DSSDK_LIBRARIES) 
** WARNING ** io features related to dssdk will be disabled
** WARNING ** io features related to pcap will be disabled
** WARNING ** io features related to png will be disabled
-- The imported target "vtkRenderingPythonTkWidgets" references the file
   "/usr/lib/aarch64-linux-gnu/libvtkRenderingPythonTkWidgets.so"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/cmake/vtk-6.3/VTKTargets.cmake"
but not all the files it references.

-- The imported target "vtk" references the file
   "/usr/bin/vtk"
but this file does not exist.  Possible reasons include:
* The file was deleted, renamed, or moved to another location.
* An install or uninstall procedure did not complete successfully.
* The installation package was faulty and contained
   "/usr/lib/cmake/vtk-6.3/VTKTargets.cmake"
but not all the files it references.

** WARNING ** io features related to libusb-1.0 will be disabled
-- Could NOT find ensenso (missing: ENSENSO_LIBRARY ENSENSO_INCLUDE_DIR) 
** WARNING ** visualization features related to ensenso will be disabled
-- Could NOT find DAVIDSDK (missing: DAVIDSDK_LIBRARY DAVIDSDK_INCLUDE_DIR) 
** WARNING ** visualization features related to davidSDK will be disabled
-- Could NOT find DSSDK (missing: _DSSDK_LIBRARIES) 
** WARNING ** visualization features related to dssdk will be disabled
-- Could NOT find RSSDK (missing: _RSSDK_LIBRARIES) 
** WARNING ** visualization features related to rssdk will be disabled
-- looking for PCL_COMMON
-- looking for PCL_OCTREE
-- looking for PCL_IO
-- looking for PCL_KDTREE
-- looking for PCL_SEARCH
-- looking for PCL_SAMPLE_CONSENSUS
-- looking for PCL_FILTERS
-- looking for PCL_2D
-- looking for PCL_GEOMETRY
-- looking for PCL_FEATURES
-- looking for PCL_ML
-- looking for PCL_SEGMENTATION
-- looking for PCL_VISUALIZATION
-- looking for PCL_SURFACE
-- looking for PCL_REGISTRATION
-- looking for PCL_KEYPOINTS
-- looking for PCL_TRACKING
-- looking for PCL_RECOGNITION
-- looking for PCL_STEREO
-- looking for PCL_APPS
-- looking for PCL_IN_HAND_SCANNER
-- looking for PCL_MODELER
-- looking for PCL_POINT_CLOUD_EDITOR
-- looking for PCL_OUTOFCORE
-- looking for PCL_PEOPLE
-- +++ processing catkin package: 'realsense2_camera'
-- ==> add_subdirectory(realsense-ros/realsense2_camera)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- Create Release Build.
-- realsense2_camera: 2 messages, 0 services
-- +++ processing catkin package: 'UT395B'
-- ==> add_subdirectory(UT395B)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
-- +++ processing catkin package: 'usb_cam'
-- ==> add_subdirectory(usb_cam)
-- +++ processing catkin package: 'mobile_robot_2dnav'
-- ==> add_subdirectory(mobile_robot_2dnav)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- +++ processing catkin package: 'azure_kinect_ros_driver'
-- ==> add_subdirectory(Azure_Kinect_ROS_Driver)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
Finding K4A SDK binaries
!!! Body Tracking SDK not found: body tracking features will not be available !!!
K4A Libs: k4a::k4a;k4a::k4arecord
K4A DLLs: /usr/lib/aarch64-linux-gnu/libk4a.so.1.4.1;/usr/lib/aarch64-linux-gnu/libk4arecord.so.1.4.1
K4A Install Needed: FALSE
-- +++ processing catkin package: 'xbox_node'
-- ==> add_subdirectory(xbox_node)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/robocon/catkin_ws/build
####
#### Running command: "make -j6 -l6" in "/home/robocon/catkin_ws/build"
####
[  0%] Built target std_msgs_generate_messages_lisp
[  0%] Built target std_msgs_generate_messages_eus
[  0%] Built target sensor_msgs_generate_messages_py
[  0%] Built target std_msgs_generate_messages_cpp
[  0%] Built target std_msgs_generate_messages_nodejs
[  0%] Built target std_msgs_generate_messages_py
[  0%] Built target geometry_msgs_generate_messages_nodejs
[  0%] Built target geometry_msgs_generate_messages_eus
[  0%] Built target geometry_msgs_generate_messages_cpp
[  0%] Built target sensor_msgs_generate_messages_eus
[  0%] Built target geometry_msgs_generate_messages_py
[  0%] Built target sensor_msgs_generate_messages_lisp
[  0%] Built target sensor_msgs_generate_messages_cpp
[  0%] Built target geometry_msgs_generate_messages_lisp
[  0%] Built target sensor_msgs_generate_messages_nodejs
[  0%] Built target diagnostic_msgs_generate_messages_py
[  1%] Building CXX object iai_kinect2_opencv4/kinect2_registration/CMakeFiles/kinect2_registration.dir/src/kinect2_registration.cpp.o
[  1%] Built target _catkin_empty_exported_target
[  1%] Built target _ds4_driver_generate_messages_check_deps_Trackpad
[  1%] Built target _ds4_driver_generate_messages_check_deps_Feedback
[  1%] Built target rosgraph_msgs_generate_messages_py
[  1%] Built target _ds4_driver_generate_messages_check_deps_Status
[  1%] Built target _ds4_driver_generate_messages_check_deps_Report
[  2%] Building CXX object iai_kinect2_opencv4/kinect2_registration/CMakeFiles/kinect2_registration.dir/src/depth_registration_cpu.cpp.o
[  2%] Built target rosgraph_msgs_generate_messages_nodejs
[  4%] Building CXX object iai_kinect2_opencv4/kinect2_registration/CMakeFiles/kinect2_registration.dir/src/depth_registration_opencl.cpp.o
[  4%] Built target rosgraph_msgs_generate_messages_lisp
[  4%] Built target rosgraph_msgs_generate_messages_eus
[  4%] Built target roscpp_generate_messages_cpp
[  4%] Built target rosgraph_msgs_generate_messages_cpp
[  4%] Built target roscpp_generate_messages_lisp
[  4%] Built target roscpp_generate_messages_eus
[  4%] Built target roscpp_generate_messages_nodejs
[  4%] Built target roscpp_generate_messages_py
[  4%] Built target dynamic_reconfigure_gencfg
[  4%] Built target tf2_msgs_generate_messages_cpp
[  4%] Built target actionlib_msgs_generate_messages_lisp
[  4%] Built target actionlib_generate_messages_py
[  4%] Built target actionlib_msgs_generate_messages_nodejs
[  4%] Built target actionlib_generate_messages_nodejs
[  4%] Built target actionlib_generate_messages_eus
[  4%] Built target tf_generate_messages_py
[  4%] Built target nodelet_generate_messages_eus
[  4%] Built target actionlib_msgs_generate_messages_cpp
[  4%] Built target actionlib_generate_messages_cpp
[  4%] Built target tf_generate_messages_cpp
[  4%] Built target actionlib_msgs_generate_messages_eus
[  4%] Built target nodelet_generate_messages_lisp
[  4%] Built target actionlib_msgs_generate_messages_py
[  4%] Built target tf_generate_messages_lisp
[  4%] Built target bond_generate_messages_lisp
[  4%] Built target tf2_msgs_generate_messages_eus
[  4%] Built target tf_generate_messages_nodejs
[  4%] Built target tf2_msgs_generate_messages_lisp
[  4%] Built target tf2_msgs_generate_messages_nodejs
[  4%] Built target tf2_msgs_generate_messages_py
[  4%] Built target actionlib_generate_messages_lisp
[  4%] Built target bond_generate_messages_py
[  4%] Built target nodelet_generate_messages_cpp
[  4%] Built target nodelet_generate_messages_nodejs
[  4%] Built target nodelet_generate_messages_py
[  4%] Built target bond_generate_messages_nodejs
[  4%] Built target tf_generate_messages_eus
[  4%] Built target dynamic_reconfigure_generate_messages_lisp
[  4%] Built target bond_generate_messages_cpp
[  4%] Built target dynamic_reconfigure_generate_messages_nodejs
[  4%] Built target bond_generate_messages_eus
[  4%] Built target dynamic_reconfigure_generate_messages_cpp
[  4%] Built target dynamic_reconfigure_generate_messages_py
[  4%] Built target dynamic_reconfigure_generate_messages_eus
[  4%] Built target std_srvs_generate_messages_eus
[  4%] Built target nav_msgs_generate_messages_py
[  4%] Built target _realsense2_camera_generate_messages_check_deps_IMUInfo
[  4%] Built target std_srvs_generate_messages_lisp
[  4%] Built target _realsense2_camera_generate_messages_check_deps_Extrinsics
[  4%] Built target std_srvs_generate_messages_cpp
[  4%] Built target nav_msgs_generate_messages_lisp
[  4%] Built target nav_msgs_generate_messages_nodejs
[  4%] Built target nav_msgs_generate_messages_eus
[  4%] Built target nav_msgs_generate_messages_cpp
[  4%] Built target diagnostic_msgs_generate_messages_lisp
[  4%] Built target std_srvs_generate_messages_nodejs
[  4%] Built target std_srvs_generate_messages_py
[  4%] Built target diagnostic_msgs_generate_messages_cpp
[  4%] Built target diagnostic_msgs_generate_messages_eus
[  4%] Built target diagnostic_msgs_generate_messages_nodejs
[  5%] Generating Python from MSG realsense2_camera/IMUInfo
[  6%] Generating Javascript code from realsense2_camera/IMUInfo.msg
[  8%] Generating EusLisp code from realsense2_camera/IMUInfo.msg
[  9%] Generating Javascript code from realsense2_camera/Extrinsics.msg
[ 10%] Generating EusLisp code from realsense2_camera/Extrinsics.msg
[ 10%] Built target realsense2_camera_generate_messages_nodejs
[ 12%] Generating EusLisp manifest code for realsense2_camera
[ 13%] Generating Python from MSG realsense2_camera/Extrinsics
In file included from /home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/src/depth_registration_opencl.cpp:33:0:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: In constructor ‘cl::Image1D::Image1D(const cl::Context&, cl_mem_flags, cl::ImageFormat, size_t, void*, cl_int*)’:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:3654:9: warning: missing braces around initializer for ‘_cl_image_desc::<unnamed union>’ [-Wmissing-braces]
         };
         ^
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: In constructor ‘cl::Image1DBuffer::Image1DBuffer(const cl::Context&, cl_mem_flags, cl::ImageFormat, size_t, const cl::Buffer&, cl_int*)’:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:3740:9: warning: missing braces around initializer for ‘_cl_image_desc::<unnamed union>’ [-Wmissing-braces]
         };
         ^
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: In constructor ‘cl::Image1DArray::Image1DArray(const cl::Context&, cl_mem_flags, cl::ImageFormat, size_t, size_t, size_t, void*, cl_int*)’:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:3821:9: warning: missing braces around initializer for ‘_cl_image_desc::<unnamed union>’ [-Wmissing-braces]
         };
         ^
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: In constructor ‘cl::Image2D::Image2D(const cl::Context&, cl_mem_flags, cl::ImageFormat, size_t, size_t, size_t, void*, cl_int*)’:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:3928:13: warning: missing braces around initializer for ‘_cl_image_desc::<unnamed union>’ [-Wmissing-braces]
             };
             ^
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: In constructor ‘cl::Image2DArray::Image2DArray(const cl::Context&, cl_mem_flags, cl::ImageFormat, size_t, size_t, size_t, size_t, size_t, void*, cl_int*)’:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:4131:9: warning: missing braces around initializer for ‘_cl_image_desc::<unnamed union>’ [-Wmissing-braces]
         };
         ^
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: In constructor ‘cl::Image3D::Image3D(const cl::Context&, cl_mem_flags, cl::ImageFormat, size_t, size_t, size_t, size_t, size_t, void*, cl_int*)’:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:4241:13: warning: missing braces around initializer for ‘_cl_image_desc::<unnamed union>’ [-Wmissing-braces]
             };
             ^
In file included from /home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/src/depth_registration_opencl.cpp:33:0:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp: At global scope:
/home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_registration/include/internal/CL/cl.hpp:5113:28: warning: ignoring attributes on template argument ‘cl_int {aka int}’ [-Wignored-attributes]
         VECTOR_CLASS<cl_int>* binaryStatus = NULL,
                            ^
[ 14%] Generating Lisp code from realsense2_camera/IMUInfo.msg
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
[ 16%] Generating Lisp code from realsense2_camera/Extrinsics.msg
[ 16%] Built target realsense2_camera_generate_messages_lisp
[ 17%] Generating Python msg __init__.py for realsense2_camera
[ 18%] Building CXX object usb_cam/CMakeFiles/usb_cam.dir/src/usb_cam.cpp.o
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
[ 18%] Built target realsense2_camera_generate_messages_py
[ 20%] Building CXX object xbox_node/CMakeFiles/xbox_node.dir/src/xbox.cpp.o
[ 20%] Built target realsense2_camera_generate_messages_eus
[ 21%] Building CXX object vision_opencv/cv_bridge/src/CMakeFiles/cv_bridge.dir/cv_bridge.cpp.o
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp: In member function ‘int usb_cam::UsbCam::init_mjpeg_decoder(int, int)’:
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:386:89: warning: ‘int avpicture_alloc(AVPicture*, AVPixelFormat, int, int)’ is deprecated [-Wdeprecated-declarations]
 _alloc((AVPicture *)avframe_rgb_, AV_PIX_FMT_RGB24, image_width, image_height);
                                                                              ^
In file included from /home/robocon/catkin_ws/src/usb_cam/include/usb_cam/usb_cam.h:44:0,
                 from /home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:55:
/usr/include/aarch64-linux-gnu/libavcodec/avcodec.h:5626:5: note: declared here
 int avpicture_alloc(AVPicture *picture, enum AVPixelFormat pix_fmt, int width, int height);
     ^~~~~~~~~~~~~~~
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:397:90: warning: ‘int avpicture_get_size(AVPixelFormat, int, int)’ is deprecated [-Wdeprecated-declarations]
 mera_size_ = avpicture_get_size(AV_PIX_FMT_YUV422P, image_width, image_height);
                                                                              ^
In file included from /home/robocon/catkin_ws/src/usb_cam/include/usb_cam/usb_cam.h:44:0,
                 from /home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:55:
/usr/include/aarch64-linux-gnu/libavcodec/avcodec.h:5653:5: note: declared here
 int avpicture_get_size(enum AVPixelFormat pix_fmt, int width, int height);
     ^~~~~~~~~~~~~~~~~~
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:398:85: warning: ‘int avpicture_get_size(AVPixelFormat, int, int)’ is deprecated [-Wdeprecated-declarations]
 me_rgb_size_ = avpicture_get_size(AV_PIX_FMT_RGB24, image_width, image_height);
                                                                              ^
In file included from /home/robocon/catkin_ws/src/usb_cam/include/usb_cam/usb_cam.h:44:0,
                 from /home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:55:
/usr/include/aarch64-linux-gnu/libavcodec/avcodec.h:5653:5: note: declared here
 int avpicture_get_size(enum AVPixelFormat pix_fmt, int width, int height);
     ^~~~~~~~~~~~~~~~~~
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp: In member function ‘void usb_cam::UsbCam::mjpeg2rgb(char*, int, char*, int)’:
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:422:94: warning: ‘int avcodec_decode_video2(AVCodecContext*, AVFrame*, int*, const AVPacket*)’ is deprecated [-Wdeprecated-declarations]
 avcodec_decode_video2(avcodec_context_, avframe_camera_, &got_picture, &avpkt);
                                                                              ^
In file included from /home/robocon/catkin_ws/src/usb_cam/include/usb_cam/usb_cam.h:44:0,
                 from /home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:55:
/usr/include/aarch64-linux-gnu/libavcodec/avcodec.h:4993:5: note: declared here
 int avcodec_decode_video2(AVCodecContext *avctx, AVFrame *picture,
     ^~~~~~~~~~~~~~~~~~~~~
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:441:76: warning: ‘int avpicture_get_size(AVPixelFormat, int, int)’ is deprecated [-Wdeprecated-declarations]
   int pic_size = avpicture_get_size(avcodec_context_->pix_fmt, xsize, ysize);
                                                                            ^
In file included from /home/robocon/catkin_ws/src/usb_cam/include/usb_cam/usb_cam.h:44:0,
                 from /home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:55:
/usr/include/aarch64-linux-gnu/libavcodec/avcodec.h:5653:5: note: declared here
 int avpicture_get_size(enum AVPixelFormat pix_fmt, int width, int height);
     ^~~~~~~~~~~~~~~~~~
/home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:454:123: warning: ‘int avpicture_layout(const AVPicture*, AVPixelFormat, int, int, unsigned char*, int)’ is deprecated [-Wdeprecated-declarations]
 frame_rgb_, AV_PIX_FMT_RGB24, xsize, ysize, (uint8_t *)RGB, avframe_rgb_size_);
                                                                              ^
In file included from /home/robocon/catkin_ws/src/usb_cam/include/usb_cam/usb_cam.h:44:0,
                 from /home/robocon/catkin_ws/src/usb_cam/src/usb_cam.cpp:55:
/usr/include/aarch64-linux-gnu/libavcodec/avcodec.h:5645:5: note: declared here
 int avpicture_layout(const AVPicture *src, enum AVPixelFormat pix_fmt,
     ^~~~~~~~~~~~~~~~
[ 22%] Building CXX object vision_opencv/cv_bridge/src/CMakeFiles/cv_bridge.dir/rgb_colors.cpp.o
[ 24%] Generating Javascript code from ds4_driver/Feedback.msg
[ 25%] Generating Javascript code from ds4_driver/Report.msg
[ 26%] Generating Javascript code from ds4_driver/Status.msg
[ 28%] Generating Javascript code from ds4_driver/Trackpad.msg
[ 28%] Built target ds4_driver_generate_messages_nodejs
[ 29%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/libusb_cam.so
[ 30%] Generating C++ code from ds4_driver/Feedback.msg
[ 30%] Built target usb_cam
[ 32%] Generating EusLisp code from ds4_driver/Feedback.msg
[ 33%] Generating C++ code from ds4_driver/Report.msg
[ 34%] Generating EusLisp code from ds4_driver/Report.msg
[ 36%] Generating C++ code from ds4_driver/Status.msg
[ 37%] Generating EusLisp code from ds4_driver/Status.msg
[ 38%] Generating EusLisp code from ds4_driver/Trackpad.msg
[ 40%] Generating C++ code from ds4_driver/Trackpad.msg
[ 41%] Generating EusLisp manifest code for ds4_driver
[ 42%] Linking CXX executable /home/robocon/catkin_ws/devel/lib/xbox_node/xbox_node
[ 42%] Built target ds4_driver_generate_messages_cpp
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
[ 44%] Generating Python from MSG ds4_driver/Feedback
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
[ 44%] Built target xbox_node
[ 45%] Generating Lisp code from ds4_driver/Feedback.msg
[ 46%] Generating Lisp code from ds4_driver/Report.msg
WARNING: Package name "UT395B" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
WARNING: Package name "shooterControll" does not follow the naming conventions. It should start with a lower case letter and only contain lower case letters, digits, underscores, and dashes.
[ 48%] Generating Python from MSG ds4_driver/Report
[ 49%] Generating Lisp code from ds4_driver/Status.msg
[ 50%] Generating Lisp code from ds4_driver/Trackpad.msg
[ 50%] Built target ds4_driver_generate_messages_eus
[ 52%] Generating Python from MSG ds4_driver/Status
[ 53%] Generating Python from MSG ds4_driver/Trackpad
[ 53%] Built target ds4_driver_generate_messages_lisp
[ 54%] Building CXX object vision_opencv/image_geometry/CMakeFiles/image_geometry.dir/src/pinhole_camera_model.cpp.o
[ 56%] Building CXX object vision_opencv/image_geometry/CMakeFiles/image_geometry.dir/src/stereo_camera_model.cpp.o
[ 57%] Generating Python msg __init__.py for ds4_driver
[ 57%] Built target ds4_driver_generate_messages_py
[ 58%] Generating C++ code from realsense2_camera/IMUInfo.msg
[ 60%] Building CXX object usb_cam/CMakeFiles/usb_cam_node.dir/nodes/usb_cam_node.cpp.o
[ 61%] Generating C++ code from realsense2_camera/Extrinsics.msg
[ 62%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/libkinect2_registration.so
[ 62%] Built target realsense2_camera_generate_messages_cpp
[ 62%] Built target ds4_driver_generate_messages
[ 62%] Built target kinect2_registration
[ 62%] Built target realsense2_camera_generate_messages
[ 64%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/libcv_bridge.so
[ 64%] Built target cv_bridge
[ 65%] Building CXX object vision_opencv/cv_bridge/src/CMakeFiles/cv_bridge_boost.dir/module.cpp.o
[ 66%] Building CXX object iai_kinect2_opencv4/kinect2_bridge/CMakeFiles/kinect2_bridge.dir/src/kinect2_bridge.cpp.o
[ 68%] Building CXX object iai_kinect2_opencv4/kinect2_calibration/CMakeFiles/kinect2_calibration.dir/src/kinect2_calibration.cpp.o
[ 69%] Building CXX object iai_kinect2_opencv4/kinect2_bridge/CMakeFiles/kinect2_bridge_nodelet.dir/src/kinect2_bridge.cpp.o
[ 70%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/libimage_geometry.so
[ 70%] Built target image_geometry
[ 72%] Building CXX object vision_opencv/cv_bridge/src/CMakeFiles/cv_bridge_boost.dir/module_opencv.cpp.o
[ 73%] Linking CXX executable /home/robocon/catkin_ws/devel/lib/usb_cam/usb_cam_node
[ 73%] Built target usb_cam_node
[ 74%] Building CXX object iai_kinect2_opencv4/kinect2_viewer/CMakeFiles/kinect2_viewer.dir/src/viewer.cpp.o
In file included from /home/robocon/catkin_ws/src/vision_opencv/cv_bridge/src/module.cpp:35:0:
/home/robocon/catkin_ws/src/vision_opencv/cv_bridge/src/module.hpp: In function ‘int do_numpy_import()’:
/home/robocon/catkin_ws/src/vision_opencv/cv_bridge/src/module.hpp:39:5: warning: converting to non-pointer type ‘int’ from NULL [-Wconversion-null]
     import_array( );
     ^~~~~~~~~~~~
In file included from /home/robocon/catkin_ws/src/vision_opencv/cv_bridge/src/module_opencv.cpp:3:0:
/home/robocon/catkin_ws/src/vision_opencv/cv_bridge/src/module.hpp: In function ‘int do_numpy_import()’:
/home/robocon/catkin_ws/src/vision_opencv/cv_bridge/src/module.hpp:39:5: warning: converting to non-pointer type ‘int’ from NULL [-Wconversion-null]
     import_array( );
     ^~~~~~~~~~~~
In file included from /usr/include/pcl-1.8/pcl/visualization/impl/pcl_visualizer.hpp:48:0,
                 from /usr/include/pcl-1.8/pcl/visualization/pcl_visualizer.h:2262,
                 from /usr/include/pcl-1.8/pcl/visualization/cloud_viewer.h:39,
                 from /home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_viewer/src/viewer.cpp:32:
/usr/include/vtk-6.3/vtkMath.h:664:3: warning: multi-line comment [-Wcomment]
   // a & b \\
   ^
/usr/include/vtk-6.3/vtkMath.h:668:3: warning: multi-line comment [-Wcomment]
   // 1 & 0 \\
   ^
/usr/include/vtk-6.3/vtkMath.h:671:3: warning: multi-line comment [-Wcomment]
   // a & b \\
   ^
Scanning dependencies of target realsense2_camera
[ 76%] Building CXX object realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera.dir/src/realsense_node_factory.cpp.o
[ 77%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/python3/dist-packages/cv_bridge/boost/cv_bridge_boost.so
[ 77%] Built target cv_bridge_boost
[ 78%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_node.dir/src/k4a_ros_bridge_node.cpp.o
[ 80%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_node.dir/src/k4a_ros_device.cpp.o
In file included from /home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_viewer/src/viewer.cpp:32:0:
/usr/include/pcl-1.8/pcl/visualization/cloud_viewer.h:202:14: warning: ‘template<class> class std::auto_ptr’ is deprecated [-Wdeprecated-declarations]
         std::auto_ptr<CloudViewer_impl> impl_;
              ^~~~~~~~
In file included from /usr/include/c++/7/memory:80:0,
                 from /usr/include/c++/7/thread:39,
                 from /home/robocon/catkin_ws/src/iai_kinect2_opencv4/kinect2_viewer/src/viewer.cpp:26:
/usr/include/c++/7/bits/unique_ptr.h:51:28: note: declared here
   template<typename> class auto_ptr;
                            ^~~~~~~~
[ 81%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/libkinect2_bridge_nodelet.so
[ 82%] Linking CXX executable /home/robocon/catkin_ws/devel/lib/kinect2_bridge/kinect2_bridge
[ 82%] Built target kinect2_bridge_nodelet
[ 84%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_nodelet.dir/src/k4a_ros_bridge_nodelet.cpp.o
/usr/bin/ld: warning: libopencv_flann.so.3.2, needed by /usr/lib/aarch64-linux-gnu/libopencv_calib3d.so.3.2.0, may conflict with libopencv_flann.so.4.5
/usr/bin/ld: warning: libopencv_imgproc.so.4.5, needed by /usr/local/lib/libopencv_imgcodecs.so.4.5.2, may conflict with libopencv_imgproc.so.3.2
/usr/bin/ld: warning: libopencv_calib3d.so.4.5, needed by /home/robocon/catkin_ws/devel/lib/libkinect2_registration.so, may conflict with libopencv_calib3d.so.3.2
[ 84%] Built target kinect2_bridge
[ 85%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_node.dir/src/k4a_ros_device_params.cpp.o
[ 86%] Linking CXX executable /home/robocon/catkin_ws/devel/lib/kinect2_calibration/kinect2_calibration
/usr/bin/ld: warning: libopencv_flann.so.3.2, needed by /usr/lib/aarch64-linux-gnu/libopencv_calib3d.so.3.2.0, may conflict with libopencv_flann.so.4.5
/usr/bin/ld: warning: libopencv_imgcodecs.so.3.2, needed by /usr/lib/aarch64-linux-gnu/libopencv_highgui.so.3.2.0, may conflict with libopencv_imgcodecs.so.4.5
/usr/bin/ld: warning: libopencv_imgproc.so.4.5, needed by /home/robocon/catkin_ws/devel/lib/libcv_bridge.so, may conflict with libopencv_imgproc.so.3.2
/usr/bin/ld: warning: libopencv_calib3d.so.4.5, needed by /home/robocon/catkin_ws/devel/lib/libkinect2_registration.so, may conflict with libopencv_calib3d.so.3.2
/usr/bin/ld: warning: libopencv_features2d.so.4.5, needed by /usr/local/lib/libopencv_calib3d.so.4.5.2, may conflict with libopencv_features2d.so.3.2
[ 86%] Built target kinect2_calibration
[ 88%] Building CXX object realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera.dir/src/base_realsense_node.cpp.o
[ 89%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_node.dir/src/k4a_calibration_transform_data.cpp.o
[ 90%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_nodelet.dir/src/k4a_ros_device.cpp.o
[ 92%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_nodelet.dir/src/k4a_ros_device_params.cpp.o
[ 93%] Linking CXX executable /home/robocon/catkin_ws/devel/lib/azure_kinect_ros_driver/node
[ 93%] Built target azure_kinect_ros_driver_node
[ 94%] Building CXX object realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera.dir/src/t265_realsense_node.cpp.o
[ 96%] Building CXX object Azure_Kinect_ROS_Driver/CMakeFiles/azure_kinect_ros_driver_nodelet.dir/src/k4a_calibration_transform_data.cpp.o
[ 97%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/libazure_kinect_ros_driver_nodelet.so
[ 97%] Built target azure_kinect_ros_driver_nodelet
[ 98%] Linking CXX executable /home/robocon/catkin_ws/devel/lib/kinect2_viewer/kinect2_viewer
/usr/bin/ld: warning: libopencv_flann.so.3.2, needed by /usr/lib/aarch64-linux-gnu/libopencv_calib3d.so.3.2.0, may conflict with libopencv_flann.so.4.5
/usr/bin/ld: warning: libopencv_imgcodecs.so.3.2, needed by /usr/lib/aarch64-linux-gnu/libopencv_highgui.so.3.2.0, may conflict with libopencv_imgcodecs.so.4.5
/usr/bin/ld: warning: libopencv_calib3d.so.4.5, needed by /home/robocon/catkin_ws/devel/lib/libkinect2_registration.so, may conflict with libopencv_calib3d.so.3.2
[ 98%] Built target kinect2_viewer
[100%] Linking CXX shared library /home/robocon/catkin_ws/devel/lib/librealsense2_camera.so
[100%] Built target realsense2_camera
