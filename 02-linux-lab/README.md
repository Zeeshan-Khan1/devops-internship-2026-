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
