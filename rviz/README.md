# 🤖 Robot197 – ROS 2 Robot Description & Control

Robot197 is a **ROS 2–based robotics project** that demonstrates a clean separation between **robot description** (URDF/Xacro, meshes, RViz) and **robot control** (Python ROS 2 nodes).

This repository is part of my long-term journey toward becoming a **professional robotics engineer**, focusing on **realistic ROS architecture, clean package design, and reproducible visualization**.

---

## 📦 Project Structure

```text
ros2_ws/src/                         #the ros2_ws is the stating folder for the linux terminal. create src folder inside it.
├── my_robot_description/            #go to the linux terminal and move upto src(like cd ros2_ws and again cd src)
│   ├── urdf/                        #then create this two pkg list.
│   │   └── robot197.xacro           #like:- inside src(ros2 pkg create --build-type ament-python my_robot_description) same process for the another also
│   ├── meshes/                      #and just follow this pathing and put all the required file in proper folder
│   │   └── head197.stl, ....        #after that back to ros2_ws and colcon build
│   ├── launch/
│   │   └── display.launch.py
│   ├── CMakeLists.txt
│   └── package.xml
│
├── robot197_control/
│   ├── robot197_control/
│   │   └── simple_controller.py
│   ├── launch/
│   │   └── bringup.launch.py
│   ├── package.xml
│   ├── setup.py
│   └── setup.cfg


🧠 Architecture Overview

This project follows ROS best practices by separating responsibilities:

🔹 my_robot_description

Responsible for:

Robot geometry (URDF / Xacro)

Mesh files

TF tree via robot_state_publisher

RViz visualization

It does not contain control logic.

🔹 robot197_control

Responsible for:

Python-based ROS 2 control nodes

Publishing joint commands

Driving robot motion

It does not load URDF files directly and instead relies on the ROS graph.

🔁 Runtime Data Flow
URDF/Xacro
   ↓
robot_state_publisher
   ↓
/robot_description
   ↓
TF tree
   ↓
robot197_control (publishes joint commands)

🚀 How to Build
cd ~/ros2_ws
colcon build
source install/setup.bash

▶️ How to Run
1️⃣ Launch Robot Description (URDF + RViz)
ros2 launch my_robot_description display.launch.py

This starts:
robot_state_publisher
RViz with saved configuration

2️⃣ Launch Robot Control Node
ros2 launch robot197_control bringup.launch.py

This starts:
Python controller node
Joint motion logic

🖥️ Visualization

The RViz configuration is version-controlled and located at:

my_robot_description/rviz/robot197.rviz


This ensures consistent visualization across systems.

🛠️ Technologies Used

ROS 2 (Humble)

Python (rclpy)

URDF / Xacro

RViz 2

Git / GitHub

🎯 Learning Goals

Understand ROS 2 package architecture

Separate description and control cleanly

Work with TF, joint states, and controllers

Build a strong robotics portfolio project

📌 Notes

This project focuses on ROS-side motion and visualization

Gazebo simulation is planned as a future extension

The test/ directory is intentionally omitted for clarity at this stage

👤 Author

Ranjan Tamang
Mechanical Engineer | Aspiring Robotics Engineer
Currently building strong foundations in ROS 2, Python, and robot modeling

⭐ Future Improvements

Gazebo / Ignition simulation

ROS 2 Control integration

Modular controller architecture

Sensor integration
