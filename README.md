# 🐼 panda_vlm_control

**Simulation and Control of the Franka Emika Panda Arm in Gazebo with Vision-Language Model Integration**

---

## 🧠 Overview

This repository builds upon [`panda_gz_moveit2`](https://github.com/AndrejOrsula/panda_gz_moveit2) to simulate and control the **Franka Emika Panda** robot arm in **Gazebo (Ignition)** and **MoveIt 2** — with an added camera and a plan to integrate a Vision-Language Model (VLM) for high-level task execution.

Developed by [Ebru Subutay](https://github.com/subutayebru) – `subutayebru@gmail.com`.

---

## 🚀 Features

- 🐼 Simulated **Franka Panda** with MoveIt 2 and Gazebo
- 🌍 Custom Gazebo world
- 📷 **Monocular camera sensor** added to the scene
- 🧠 Planned integration with a trainable **VLM** to perform manipulation tasks from natural language instructions

---

## 🗂️ Repository Structure  (ADJUST)
panda_vlm_control/
├── launch/ # Simulation and control launch files
├── config/ # MoveIt and controller configurations
├── urdf/ # XACRO/URDF robot description
├── worlds/ # Custom Gazebo world(s)
├── rviz/ # RViz2 config
├── scripts/ # (Future) Python scripts for VLM control
├── meshes/ # Panda model meshes
├── CMakeLists.txt
├── package.xml
├── setup.py # Python install 
└── README.md


---

## 📦 Dependencies

- **ROS 2 Humble**
- **Gazebo Fortress** (Ignition Gazebo)
- **MoveIt 2**
- `ros_gz` (for ROS 2-Gazebo bridges)

> ⚠️ Use Gazebo Fortress (Ignition) – not Classic Gazebo.

---

## 🛠️ Installation

```bash
# Clone the repo
mkdir -p ~/ws_franka/src
cd ~/ws_franka/src
git clone https://github.com/subutayebru/panda_vlm_control.git
cd ..

# Install dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build --symlink-install

# Source the workspace
source install/setup.bash


🙏 Acknowledgements

Based on Andrej Orsula's panda_gz_moveit2 packages.
