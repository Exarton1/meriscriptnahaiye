import subprocess
import os

# --- COLORS ---
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run(cmd):
    subprocess.run(cmd, shell=True)

def banner():
    os.system("clear")
    print(f"""{CYAN}
  _   _           _     _____                 _                                  _   
 | \ | |         | |   |  __ \               | |                                | |  
 |  \| | _____  _| |_  | |  | | _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_ 
 | . ` |/ _ \ \/ / __| | |  | |/ _ \ \ / / _ \ |/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
 | |\  |  __/>  <| |_  | |__| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_ 
 |_| \_|\___/_/\_\\__| |_____/ \___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
                                                     | |                             
                                                     |_|                             
{YELLOW}🔥 SUPAR GOD MODE VPS & NETWORK OPTIMIZER ⚡
             🛡 MADE BY NINJA
{RESET}
""")

def optimize_network_ram_disk():
    print(f"{GREEN}🚀 MAX Boosting Network, RAM, Disk, VPS...{RESET}")
    cmds = [
        # Load BBR TCP Congestion Control
        "modprobe tcp_bbr",
        "echo 'tcp_bbr' | tee -a /etc/modules-load.d/modules.conf",
        "echo 'net.core.default_qdisc=fq' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf",

        # TCP Optimizations
        "echo 'net.ipv4.tcp_fastopen=3' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_mtu_probing=1' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_sack=1' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_window_scaling=1' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_timestamps=1' >> /etc/sysctl.conf",
        "echo 'net.core.rmem_max=67108864' >> /etc/sysctl.conf",
        "echo 'net.core.wmem_max=67108864' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_rmem=4096 87380 67108864' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_wmem=4096 65536 67108864' >> /etc/sysctl.conf",

        # Buffer settings
        "echo 'net.core.netdev_max_backlog=5000' >> /etc/sysctl.conf",
        "echo 'net.core.somaxconn=1024' >> /etc/sysctl.conf",

        # Memory optimization
        "echo 'vm.swappiness=10' >> /etc/sysctl.conf",
        "echo 'vm.dirty_ratio=10' >> /etc/sysctl.conf",
        "echo 'vm.dirty_background_ratio=5' >> /etc/sysctl.conf",
        "echo 'vm.overcommit_memory=1' >> /etc/sysctl.conf",
        "echo 'vm.vfs_cache_pressure=50' >> /etc/sysctl.conf",

        # File descriptors
        "ulimit -n 1048576",
        "echo 'fs.file-max=2097152' >> /etc/sysctl.conf",

        # Kill IPv6
        "echo 'net.ipv6.conf.all.disable_ipv6=1' >> /etc/sysctl.conf",
        "echo 'net.ipv6.conf.default.disable_ipv6=1' >> /etc/sysctl.conf",

        # Boost disk I/O
        "echo 'deadline' > /sys/block/sda/queue/scheduler || true",

        # Flush DNS and set fastest resolvers
        "systemd-resolve --flush-caches",
        "rm -f /etc/resolv.conf",
        "echo 'nameserver 1.1.1.1' > /etc/resolv.conf",
        "echo 'nameserver 8.8.8.8' >> /etc/resolv.conf",
        "echo 'nameserver 9.9.9.9' >> /etc/resolv.conf",

        # Apply settings
        "sysctl -p"
    ]
    for cmd in cmds:
        run(f"sudo bash -c \"{cmd}\"")
    print(f"{GREEN}✅ MAX Network, RAM, Disk Optimization Done.{RESET}\n")

def deep_clean_system():
    print(f"{YELLOW}🧹 Deep Cleaning System, Saving Money...{RESET}")
    if not is_linux():
        print(f"{RED}This script is for Linux systems only.{RESET}")
        return
    if not is_root():
        print(f"{RED}Please run this script as root (sudo).{RESET}")
        return
    if not has_cmd("apt"):
        print(f"{RED}This script requires apt (Debian/Ubuntu).{RESET}")
        return

    print(f"{YELLOW}Some actions are destructive and may disable logging, remove packages, or break apps. Proceed with caution!{RESET}")
    if not confirm("Continue with deep cleaning?"):
        print(f"{RED}Aborted by user.{RESET}")
        return

    cmds = [
        # Update & clean
        "apt update && apt upgrade -y",
        "apt autoremove --purge -y && apt autoclean -y",
    ]
    # Remove snaps, lxd if present
    if has_cmd("snap"):  # Only if snap is installed
        if confirm("Remove snapd, lxd, and related directories? This may break snap apps."):
            cmds += [
                "apt purge -y snapd lxd lxd-client",
                "rm -rf ~/snap /snap /var/snap /var/lib/snapd"
            ]
    # Disable services if present
    disable_services = ["bluetooth", "cups", "avahi-daemon", "ModemManager", "ufw", "rsyslog", "cron", "apport", "snapd", "systemd-timesyncd"]
    for svc in disable_services:
        if has_cmd("systemctl"):
            safe_run(f"systemctl disable --now {svc}")
    # Logging warning
    if confirm("Disable and clean system logs (rsyslog, journald)? This may make troubleshooting harder."):
        cmds += [
            "journalctl --vacuum-time=1d",
            "sed -i 's/#SystemMaxUse=.*/SystemMaxUse=30M/' /etc/systemd/journald.conf",
            "systemctl restart systemd-journald"
        ]
    # Remove old kernels (safe, but only on apt systems)
    cmds.append("dpkg --list | grep linux-image | awk '{print $2}' | grep -v $(uname -r) | xargs sudo apt purge -y")
    # Empty Trash and Cache (warn user)
    if confirm("Remove all user and root cache/tmp files? This may delete unsaved work in /tmp."):
        cmds.append("rm -rf ~/.cache/* /var/tmp/* /tmp/* /root/.cache/*")
    # Clear bash history (optional)
    if confirm("Clear bash history for all users?"):
        cmds.append("history -c && history -w")
    # Set no GUI
    if has_cmd("systemctl"):
        cmds.append("systemctl set-default multi-user.target")
    # Force CPU governor
    if has_cmd("cpufrequtils") or confirm("Install/force CPU governor to performance? (Installs cpufrequtils)"):
        cmds += [
            "apt install -y cpufrequtils",
            "echo 'GOVERNOR=\"performance\"' > /etc/default/cpufrequtils",
            "systemctl restart cpufrequtils"
        ]
    # Restart services
    if has_cmd("systemctl"):
        cmds.append("systemctl daemon-reexec")

    for cmd in cmds:
        print(f"{CYAN}Running: {cmd}{RESET}")
        safe_run(f"sudo bash -c \"{cmd}\"")
    print(f"{YELLOW}✅ System Deep Clean and Slimming Done!{RESET}\n")

def full_god_optimize():
    optimize_network_ram_disk()
    deep_clean_system()

def security_hardening():
    print(f"{YELLOW}🔒 Security Hardening (Firewall, SSH, Fail2Ban)...{RESET}")
    if not is_linux():
        print(f"{RED}This script is for Linux systems only.{RESET}")
        return
    if not is_root():
        print(f"{RED}Please run this script as root (sudo).{RESET}")
        return
    # UFW setup
    if has_cmd("ufw") or confirm("Install UFW firewall?"):
        safe_run("apt install -y ufw")
        safe_run("ufw default deny incoming")
        safe_run("ufw default allow outgoing")
        safe_run("ufw allow ssh")
        if confirm("Enable UFW firewall now? (May disrupt existing connections)"):
            safe_run("ufw --force enable")
    # SSH security
    sshd_config = "/etc/ssh/sshd_config"
    if os.path.exists(sshd_config):
        # Change SSH port
        if confirm("Change SSH port from 22? (You must update your client settings)"):
            new_port = input("Enter new SSH port (e.g., 2222): ").strip()
            if new_port.isdigit():
                safe_run(f"sed -i 's/^#Port .*/Port {new_port}/' {sshd_config}")
                safe_run(f"sed -i 's/^Port .*/Port {new_port}/' {sshd_config}")
                safe_run(f"ufw allow {new_port}/tcp")
        # Disable root login
        if confirm("Disable SSH root login?"):
            safe_run(f"sed -i 's/^#PermitRootLogin .*/PermitRootLogin no/' {sshd_config}")
            safe_run(f"sed -i 's/^PermitRootLogin .*/PermitRootLogin no/' {sshd_config}")
        # Enforce key authentication
        if confirm("Enforce SSH key authentication only?"):
            safe_run(f"sed -i 's/^#PasswordAuthentication .*/PasswordAuthentication no/' {sshd_config}")
            safe_run(f"sed -i 's/^PasswordAuthentication .*/PasswordAuthentication no/' {sshd_config}")
        # Limit login attempts
        if confirm("Limit SSH login attempts (MaxAuthTries)?"):
            tries = input("Enter max SSH auth tries (default 3): ").strip() or "3"
            safe_run(f"sed -i 's/^#MaxAuthTries .*/MaxAuthTries {tries}/' {sshd_config}")
            safe_run(f"sed -i 's/^MaxAuthTries .*/MaxAuthTries {tries}/' {sshd_config}")
        print(f"{CYAN}Restarting SSH service...{RESET}")
        safe_run("systemctl restart sshd || systemctl restart ssh")
    # Fail2Ban setup
    if has_cmd("fail2ban-client") or confirm("Install Fail2Ban for SSH brute-force protection?"):
        safe_run("apt install -y fail2ban")
        safe_run("systemctl enable fail2ban --now")
        print(f"{GREEN}Fail2Ban is now running. Default jail protects SSH.{RESET}")
    print(f"{GREEN}✅ Security Hardening Complete!{RESET}\n")

def menu():
    banner()
    print(f"{CYAN}Choose your GOD MODE OPTIMIZATION:{RESET}")
    print(f"{GREEN}1️⃣  MAX Network, RAM, Disk Boost ⚡")
    print(f"2️⃣  DEEP Clean VPS (Save Money 💸)")
    print(f"{RED}3️⃣  FULL SUPAR GOD MODE (Everything) 🚀")
    print(f"{YELLOW}4️⃣  SECURITY Hardening (Firewall & SSH & Fail2Ban){RESET}\n")

    choice = input("Enter choice [1-4]: ").strip()
    if choice == "1":
        optimize_network_ram_disk()
    elif choice == "2":
        deep_clean_system()
    elif choice == "3":
        full_god_optimize()
    elif choice == "4":
        security_hardening()
    else:
        print(f"{RED}❌ Invalid selection.{RESET}")

if __name__ == "__main__":
    menu()