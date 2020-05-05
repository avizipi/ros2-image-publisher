# ros2-image-publisher
tutorial for image publishing in ROS1 and ROS2


to run the ros1 image publisher use this commands:
open roscore and in a new terminal run:
cd image_publisher_ros_workspace 
catkin_make
source devel/setup.bash
rosrun image_publisher image_publisher.py

to run the ros2 image publisher use this commands:
cd image_publisher_ros2_workspace 
colcon build --symlink-install
source install/setup.bash
ros2 run image_publisher run_simple_image_pub
