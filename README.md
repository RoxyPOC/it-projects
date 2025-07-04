# it-projects

https://roxypoc.github.io/it-projects/

# 🔁 File Backup Script

## 📝 Overview
This is a simple Python script that backs up files from a source folder to a destination folder. It was built to practice basic file handling and automation using Python's built-in libraries.

## 🛠 Tech Used
- Python 3
- os
- shutil

## 🚀 How It Works
- Loops through all files in the source folder
- Copies each file to the destination folder
- Prints a confirmation message once complete

## 🔧 How to Use
1. Update the `source` and `destination` folder paths in the script.
2. Run it using your terminal:
   ```bash
   python backup.py

   
---

## 💾 2. `vm-lab-notes` — README.md

```markdown
# 💾 Windows 10 VM Lab

## 🧪 Overview
This project documents my setup and testing of a Windows 10 virtual environment using VirtualBox. It includes configuration notes, system restore checkpoints, and sample troubleshooting tasks.

## 🛠 Tools Used
- VirtualBox
- Windows 10 ISO
- Notepad++ / Markdown

## 🔧 Lab Objectives
- Create and configure a Windows 10 VM
- Practice OS installation and snapshot rollbacks
- Simulate real-world troubleshooting (e.g., user setup, permission changes)

## ✅ Key Tasks Completed
- Installed guest additions and configured shared folders
- Created a local user account and modified permissions
- Rolled back to snapshot after testing system settings

## 🧠 What I Learned
- Managing virtual machines for safe testing environments
- Practicing Windows OS setup from scratch
- Documenting IT troubleshooting processes like a tech pro

# 🌐 Home Network Monitoring Lab

## 📡 Overview
This project demonstrates how I built and monitored a basic home network using router settings and network scanning tools like `nmap`.

## 🛠 Tools Used
- Local router admin panel (192.168.0.1)
- nmap
- Angry IP Scanner
- Windows CMD / Linux Terminal

## 🔧 What I Did
- Changed default router credentials & SSID
- Set up DHCP reservations for specific devices
- Scanned network for active IP addresses using `nmap`
- Identified unknown devices and monitored basic traffic

## 💡 Sample nmap Command
```bash
nmap -sn 192.168.1.0/24

