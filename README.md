# SUPAR GOD MODE VPS & NETWORK OPTIMIZER

## Overview
This is a powerful Python script to optimize, clean, and tune your Linux VPS for maximum performance and minimal resource waste. It automates advanced sysadmin tasks for network, RAM, disk, and system cleaning, with interactive confirmations for safety.

> **Warning:** This script is intended for advanced users on Debian/Ubuntu VPSes. It performs destructive actions and should not be run on production systems without a full understanding of the consequences.

## Features
- Aggressive network and TCP stack optimization
- RAM, disk, and kernel parameter tuning
- Deep cleaning of system: removes unused packages, disables unnecessary services, cleans logs and cache
- Interactive confirmations before any destructive action
- Platform and privilege checks to prevent accidental misuse
- Colorful, user-friendly CLI menu

## Requirements
- **Linux** system (Debian/Ubuntu recommended)
- **Python 3**
- Must be run as **root** (with `sudo`)

## Usage
1. **Upload `1.py` to your VPS.**
2. **Run the script as root:**
   ```bash
   sudo python3 1.py
   ```
3. **Follow the on-screen menu and prompts.**
   - The script will ask for confirmation before any risky operation.

## Menu Options
- **1️⃣  MAX Network, RAM, Disk Boost**
  - Tunes kernel and network parameters, disables IPv6, optimizes disk scheduler and DNS, increases file limits, etc.
- **2️⃣  DEEP Clean VPS (Save Money 💸)**
  - Updates system, removes unused packages, disables and removes unnecessary services, cleans logs and cache, sets system to CLI mode, and more.
- **3️⃣  FULL SUPAR GOD MODE (Everything) 🚀**
  - Runs both optimization and deep cleaning routines.

## Safety Warnings
- **Destructive actions:** The script may remove packages, disable logging/security services, and overwrite system files (e.g., DNS, cache, logs).
- **Not for production:** Do not run on critical systems without a backup.
- **Test first:** Always review the code and test in a safe environment before use.

## Disclaimer
This script is provided as-is with no warranty. Use at your own risk. The author is not responsible for any damage or data loss resulting from its use.

---

**Made by NINJA. Enhanced for safety and robustness.**
