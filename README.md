# Cisco Network Automation Framework
# 🚀 Cisco Network Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Cisco IOS](https://img.shields.io/badge/Cisco-IOS-1BA0D7)
![Netmiko](https://img.shields.io/badge/Netmiko-Network_Automation-green)
![Paramiko](https://img.shields.io/badge/Paramiko-SSH-orange)
![PyYAML](https://img.shields.io/badge/PyYAML-YAML-red)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-yellow)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github)

A modular Python-based network automation project for Cisco IOS devices using **Paramiko**, **Netmiko**, **PyYAML**, and **Jinja2**. This repository documents my learning journey from basic SSH connectivity to building an integrated automation workflow with inventory management, configuration templating, automated deployment, device information collection, and configuration backups.

## Overview
---

# 📖 About the Project

The **Cisco Network Automation Framework** is a hands-on Python project developed to learn and apply modern network automation techniques for Cisco IOS devices.

The project demonstrates how repetitive network administration tasks can be automated using Python and industry-standard libraries such as **Paramiko**, **Netmiko**, **PyYAML**, and **Jinja2**. It progresses from establishing basic SSH connectivity to building a modular automation framework capable of managing multiple devices, deploying configurations, collecting device information, and creating automated configuration backups.

This repository also documents the learning process by including expected outputs, troubleshooting notes, and a final integrated automation script, making it both a practical reference and a portfolio project.
This project demonstrates end-to-end Cisco network automation using Python.
The framework covers SSH automation, device configuration, inventory management, configuration templating, and automated backups.

---

---
# 🌟 Project Highlights

- 🔹 Automated Cisco IOS device management using Python
- 🔹 SSH communication with Paramiko and Netmiko
- 🔹 Multi-device automation using YAML inventory
- 🔹 Configuration templating with Jinja2
- 🔹 Automated running-configuration backups
- 🔹 Device information collection
- 🔹 Modular project structure
- 🔹 Detailed troubleshooting documentation
- 🔹 Expected outputs for every lab
- 🔹 Final integrated automation framework

## Technologies Used

- Python 3
- Paramiko
- Netmiko
- PyYAML
- Jinja2
- Cisco IOS
- Ubuntu WSL

---

---

# ✨ Key Features

## 🔐 Secure SSH Connectivity
- Establish SSH connections to Cisco IOS devices using Paramiko and Netmiko.

## 🌐 Multi-Device Automation
- Manage multiple routers from a single YAML inventory file.

## 📝 Configuration Templating
- Generate reusable device configurations with Jinja2 templates.

## 💾 Automated Backups
- Save router running configurations for documentation and recovery.

## 📊 Device Information Collection
- Retrieve essential device details such as hostname, software version, and interface information.

## 📂 Organized Project Structure
- Separate folders for templates, inventories, backups, logs, expected outputs, and troubleshooting notes.

## 📈 Progressive Learning Approach
- The repository follows a structured learning path from basic SSH scripting to a complete automation workflow.

---

## Project Structure

```text
Cisco_Network_Automation_Framework
├── inventory
├── templates
├── expected_outputs
├── troubleshooting_notes
├── backups
├── logs
├── final_project
└── Python scripts
```

---

## Learning Outcomes

- Python network automation
- SSH automation
- Configuration management
- Inventory management
- Template-based configuration
- Modular project development

---

## Known Limitation

The project could not demonstrate live configuration deployment because of a WSL-to-GNS3 SSH connectivity issue.

The automation logic, project structure, and scripts were completed successfully.
