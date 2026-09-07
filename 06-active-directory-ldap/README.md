# Active Directory & LDAP Lab

Hands-on lab setting up a Windows Server 2022 Domain Controller and exploring directory services with LDAP — built as part of my DevOps internship training.

## Overview

This repo documents a self-contained AD/LDAP lab built in VirtualBox. I promoted a Windows Server 2022 VM to a Domain Controller, designed an OU structure, provisioned users and security groups, and then used LDP.exe / ADSI Edit to query the directory directly over LDAP — inspecting binds, RootDSE data, DNs, and object attributes.

## Objectives

- Stand up a Windows Server 2022 Domain Controller from scratch
- Initialize an Active Directory domain with integrated DNS
- Design a realistic OU structure for departmental separation
- Provision users and role-based security groups
- Perform LDAP binds, connections, and search-filter queries against the DC
- Inspect core AD attributes: `sAMAccountName`, `member`, `memberOf`, DN paths

## Lab Environment

| Component | Configuration |
| ---------------------- | ---------------------------- |
| Server Name | DC01 |
| Operating System | Windows Server 2022 |
| Domain | lab.local |
| IP Address | 192.168.56.10 |
| Subnet Mask | 255.255.255.0 |
| Preferred DNS | 192.168.56.10 |
| LDAP Port | 389 (unencrypted) |
| Network Adapter | VirtualBox Host-Only Adapter |
| Hypervisor | VirtualBox |

## Directory Structure (OUs)
lab.local
├── IT
├── Finance
├── HR
└── Sales


Security groups (`IT-Team`, `Finance-Team`) were created and mapped to users across these OUs to test role-based access management.

## What Was Done

### 1. Domain Controller Setup

- Installed Windows Server 2022 on VirtualBox
- Assigned a static IPv4 address and verified connectivity (`ipconfig`, `ping`)
- Installed AD DS and promoted the server to a Domain Controller
- Initialized the `lab.local` domain with integrated DNS

### 2. User & Group Management

- Provisioned test user accounts (e.g. `zeeshan.khan`, `sara.khan`, `hamza.ali`) across the OUs via Active Directory Users and Computers (ADUC)
- Created security groups `IT-Team` and `Finance-Team`
- Assigned users to groups and verified membership via the **Members** / **Member Of** tabs
- Validated user provisioning with PowerShell: `Get-ADUser -Filter * | Select Name`

### 3. LDAP Exploration

- Connected to `DC01` on port 389 using `LDP.exe`
- Retrieved **RootDSE** information (naming contexts, domain functionality level, DNS host name)
- Performed an LDAP bind using domain administrator credentials
- Ran search filters against the directory: 
  - `(objectClass=user)` → list all user objects
  - `(objectClass=group)` → list all groups
  - `(sAMAccountName=Administrator)` → isolate a specific account
- Browsed the directory tree with **ADSI Edit**, inspecting Distinguished Names (DNs), object classes, and containers (`CN=Users`, `CN=Builtin`, `OU=IT`, etc.)
- Analyzed relationship attributes `member` and `memberOf` to trace group membership

## Screenshots

Screenshots of each step (server login, IP config, ADUC user/group creation, ADSI Edit tree, LDP.exe bind and search results) are available in the full [training report PDF](./AD-LDAP-Lab-Report.pdf).

## Key Concepts

**Active Directory (AD)** — Microsoft's directory service for centralized identity management, authentication (Kerberos/NTLM), authorization, and Group Policy enforcement across a Windows domain.

**LDAP** — An open, vendor-neutral protocol used to query and manage directory data over IP. It's the "language" tools like LDP.exe and ADSI Edit use to talk to AD (or OpenLDAP) — searching objects, authenticating, and reading attributes like DNs and group membership.

## Tools Used

- Windows Server 2022
- VirtualBox
- Active Directory Users and Computers (ADUC)
- ADSI Edit
- LDP.exe
- PowerShell (`Get-ADUser`, `ipconfig`, `ping`)

## Key Takeaways

- Domain promotion and AD DS installation workflow
- Designing a clean, department-based OU hierarchy
- Role-based access via security groups
- Reading and interpreting LDAP DNs and RootDSE metadata
- Writing and running LDAP search filters to query directory objects
