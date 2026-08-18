# 5. Task 3 — Linux Administration README

# Linux Administration

## Overview

Practiced essential Linux administration commands and concepts to build a strong foundation in system administration and troubleshooting.

## Topics Covered

### Filesystem

- Linux filesystem hierarchy
- File types
- Absolute paths
- Relative paths
- File and directory navigation

### File Management

- `ls`
- `cd`
- `pwd`
- `cp`
- `mv`
- `rm`
- `mkdir`
- `touch`

### File Permissions

Practiced:

```bash
chmod
chown
chgrp
```

### File Permissions & Access Control
Understood and applied standard Linux permission bits and ownership categories:
* **Permissions:** Read (`r`), Write (`w`), Execute (`x`)
* **Target Categories:** User (`u`), Group (`g`), Others (`o`)

---

## Technical Skills & Commands Practiced

### 1. User & Group Management
Practiced managing account lifecycles, user privileges, and group assignments:
* `useradd` — Create new user accounts
* `usermod` — Modify existing user attributes and group memberships
* `userdel` — Remove user accounts and associated directories
* `groupadd` — Create security and administrative groups
* `groupdel` — Delete existing groups
* `id` — Display user and group ID details for verification

### 2. Process Control & Resource Monitoring
Monitored system utilization, inspected running processes, and managed execution states:
* `ps` / `ps aux` — View current process snapshots and detailed process trees
* `top` / `htop` — Monitor real-time system resources and CPU/RAM consumption
* `kill` / `killall` — Terminate processes using process IDs (PIDs) or process names
* `nohup` — Run commands immune to hangups and terminal disconnections

### 3. Systemd & Service Management
Learned core `systemd` concepts and practiced controlling system services:
* `systemctl` — Start, stop, restart, enable, disable, and inspect system service status

### 4. Archiving & Compression
Practiced bundling, compressing, and extracting files for backups and data transfers:
* `tar` — Create and extract tape archives
* `gzip` — Compress and decompress files
* `zip` / `unzip` — Manage standard zip archive formats

### 5. Network Diagnostics
Executed networking utilities to verify interface configurations and connectivity:
* `ip` — Inspect and configure network interfaces, addresses, and routing
* `ping` — Test network connectivity and latency to remote hosts
* `ss` — Display detailed socket and network connection statistics
* `hostname` — Inspect and set the system hostname

### 6. Memory & System Resource Diagnostics
Practiced utilities for analyzing hardware resource allocation, swap usage, and system load.

---

## Practical Work Execution
All commands and administrative workflows were practiced directly in a live Ubuntu environment.

---

## Technical Documentation
📄 **Full Internship Report:** [Download / View PDF Report](./report.pdf)
