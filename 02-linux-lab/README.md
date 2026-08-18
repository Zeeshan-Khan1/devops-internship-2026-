# Linux Lab

## Overview

Built a small Linux virtual lab using VirtualBox to practice Linux server administration, networking, remote access, file sharing, snapshots, and automated backups.

## Lab Architecture

```text
                 VirtualBox
                     |
              Host-Only Network
                     |
        +------------+------------+
        |                         |
   Ubuntu Server              Ubuntu Client
   192.168.56.10              192.168.56.20
        |                         |
        +---------- SSH -----------+
```

## Lab Components
* **Ubuntu Server VM**
* **Ubuntu Client VM(s)**
* **VirtualBox Host-Only Networking**
* **Static IP Addresses**
* **SSH (OpenSSH)**
* **Shared Folder Integration**
* **VM Snapshots**
* **Automated Shell Backups**
* **Cron Task Scheduler**

---

## Tasks Completed

### 1. Ubuntu Server
Created and configured an Ubuntu Server virtual machine to act as the primary node.

### 2. Ubuntu Clients
Created Ubuntu client virtual machines to test network communication, remote access, and administrative tasks.

### 3. Static IP Configuration
Configured static IP addresses using Netplan for both the server and client virtual machines.

**Example Topology:**
* **Server:** `192.168.56.10`
* **Client-01:** `192.168.56.20`
* **Client-02:** `192.168.56.30`

### 4. SSH Remote Access
Installed and configured OpenSSH Server on the VMs and validated secure remote access across the network.

**Example Command:**
```bash
ssh username@192.168.56.10
