# Gazebo Simulator for AIMS

# Install
1. Place this package in your `<aims_workspace>/src` directory.

2. Install the `ros_control` packages
```sh
sudo apt-get install ros-$ROS_DISTRO-ros-control ros-$ROS_DISTRO-ros-controllers
```

3. Build
```sh
cd ~/<aims_workspace>
catkin_make
source devel/setup.${SHELL##*/}
```

4. Intersection Model
Go into the models directory and run the following script:
```sh
sh ~/<aims_workspace>/src/aims_sim_gazebo/models/copy_model.sh
chmod +x models/copy_model.sh
./models/copy_model.sh
```
