# Linux Foundations & Administration

This section contains my practical Linux learning and administration work completed during my DevOps internship.

The focus was on understanding and practicing Linux command-line operations, system administration, networking, SSH, virtualization, file permissions, users and groups, and automation using Bash and Cron.

## Topics Covered

- Linux Command Line
- File and Directory Management
- File Searching
- File Permissions
- Users and Groups
- Process Management
- Disk and Memory Management
- System Administration
- Linux Networking
- SSH
- Virtualization with VirtualBox
- Bash Scripting
- Automation with Cron
- Automated Backups

## Practical Environment

- Host OS: Ubuntu Linux
- Virtualization: Oracle VirtualBox
- Server VM: Ubuntu Server
- Client VMs: Ubuntu Client
- Networking: Host-Only Adapter + NAT
- SSH: OpenSSH
- Automation: Bash + Cron

## Linux Lab

```text
                 Host Machine
                      |
                Oracle VirtualBox
                      |
              Host-Only Network
                      |
        +-------------+-------------+
        |                           |
   Ubuntu Server                Ubuntu Client
   192.168.56.10                192.168.56.20
        |
        |
   Ubuntu Client
   192.168.56.30
