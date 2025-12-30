# 🤖 Differential Drive Autonomous Navigation (ROS 2)

![ROS2](https://img.shields.io/badge/ros2-jazzy-blue) ![C++](https://img.shields.io/badge/language-C++-red) ![Python](https://img.shields.io/badge/language-Python-yellow)

## 📌 Project Overview
This repository focuses on the development and simulation of an intelligent differential-drive robot. [cite_start]While based on a standard "Bumperbot" architecture, this project serves as a research testbed for **Optimized Path Planning** and **Sensor Fusion** in complex, unstructured environments[cite: 18, 20].

[cite_start]The goal is to move beyond basic movement and implement robust localization and mapping strategies applicable to emergency response scenarios[cite: 16].

## 🧠 Key Research & Technical Features
* [cite_start]**Sensor Fusion (EKF):** Utilizing an **Extended Kalman Filter** to integrate wheel odometry and IMU data for high-precision localization[cite: 19, 66].
* [cite_start]**Dynamic Mapping:** Implementing **SLAM Toolbox** and the **Nav2** stack to generate real-time occupancy grid maps[cite: 19, 67].
* [cite_start]**Adaptive Localization:** Deploying **AMCL (Adaptive Monte Carlo Localization)** for reliable global positioning once a map is established[cite: 19, 68].
* **Intelligent Parameters:** Developed custom **C++ nodes** with parameter callbacks to allow for real-time tuning of robot behavior without recompilation.

## 🛠️ Tech Stack & Frameworks
* **Middleware:** ROS 2 (Jazzy Jalisco)[cite: 80].
* **Simulation:** Gazebo (Physics-based simulation)[cite: 65, 80].
* **Languages:** C++ (Core Logic/Drivers), Python (Launch/Navigation scripting)[cite: 79].
* **Tools:** RViz2, Git, SLAM Toolbox[cite: 80, 82].

## 📂 Repository Structure
* `/urdf`: Robot description files (XML/Xacro) including visual, collision, and inertial properties.
* `/launch`: Python-based launch scripts for automated multi-node startup.
* `/src`: C++ nodes for parameter handling and telemetry.
* `/meshes`: Custom 3D STL models for the robot chassis and sensors.

## 📖 Background & Motivation
My research project is driven by a desire to automate emergency response in regions with poor infrastructure. This project validates the algorithms being developed for the paper *"An Optimized Path Planning Technique for Collision-Free Emergency Response using Autonomous Vehicles"*.

---
