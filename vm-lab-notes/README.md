# VM Lab Notes

This project documents the setup and testing of a Windows 10 virtual environment using VirtualBox. The lab serves as a safe environment for practicing system administration tasks, troubleshooting common Windows issues, and testing configurations without affecting physical hardware.

## Project Structure

- **index.html**: Contains the main structure of the VM Lab Notes project, including the content and layout for documenting the virtual environment setup.
- **styles/main.css**: Contains the CSS styles to enhance the appearance of the `index.html` file.

## Tools Used

- [Oracle VirtualBox](https://www.virtualbox.org/) (Version 6.1+ recommended)
- Windows 10 ISO (21H2 or newer)
- [Vagrant](https://www.vagrantup.com/) (Optional for automation)
- [Notepad++](https://notepad-plus-plus.org/) / Markdown editors
- [Windows Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/)

## Lab Objectives

- Create and configure a Windows 10 VM from scratch
- Practice OS installation and snapshot management
- Simulate real-world troubleshooting scenarios
- Test group policy and permission changes
- Configure virtual networking environments

## Virtual Machine Specifications

- **vCPU**: 2 cores
- **Memory**: 4GB RAM
- **Storage**: 50GB dynamically allocated
- **Network**: NAT + Host-only adapter
- **Display**: 128MB VRAM, 3D enabled

## VirtualBox Configuration

To create a new VM using the command line, use the following commands:

```bash
VBoxManage createvm --name "Win10-Lab" --ostype "Windows10_64" --register
VBoxManage modifyvm "Win10-Lab" --memory 4096 --cpus 2
VBoxManage createhd --filename "Win10.vdi" --size 50000
```