# -*- coding: UTF-8 -*-
# 404 SMART TOOL - GCP SSH SETUP (STAY-ALIVE VERSION)
# Developer : Nyein Ko Ko Aung (@nkka404)

import subprocess
import sys
import os
import requests
import time
import threading

# Basic colors
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

# 404 Banner
logo = f'''
{cyan}  ____ _   _    _    _   _ _   _ _____ _       _  _    ___  _  _   
{cyan} / ___| | | |  / \  | \ | | \ | | ____| |     | || |  / _ \| || |  
{white}| |   | |_| | / _ \ |  \| |  \| |  _| | |     | || |_| | | | || |_ 
{white}| |___|  _  |/ ___ \| |\  | |\  | |___| |___  |__   _| |_| |__   _|
{blue} \____|_| |_/_/   \_\_| \_|_| \_|_____|_____|    |_|  \___/    |_|  
{yellow} ------------------------------------------------------------------
{green}           Developed by: Nyein Ko Ko Aung (@nkka404)
{yellow} ------------------------------------------------------------------
'''

def stay_alive_loop():
    """System ကို အလုပ်လုပ်နေတယ်လို့ ထင်အောင် ၅ မိနစ်တစ်ခါ Pulse လုပ်ပေးတဲ့ Function"""
    while True:
        current_time = time.ctime()
        # Terminal မှာ စာသားတစ်ခုခု အမြဲ print ထုတ်ပေးခြင်းဖြင့် Idle ဖြစ်တာကို ကာကွယ်ပါတယ်
        print(f"\n{purple}[404-HEARTBEAT]{white} System Pulse at {current_time} - Status: Running")
        time.sleep(300) # ၅ မိနစ်တစ်ခါ

def duckdns_update(ip):
    token = "ykYdgfMLqVhHFkGQSf19ztRhp1WP3J"
    hostname = "nyeinkokoaung.dynv6.net"
    url = f"http://ipv4.dynv6.com/api/update?hostname={hostname}&ipv4={ip}&token={token}"
    try:
        r = requests.get(url, timeout=10)
        return r.text.strip()
    except:
        return "Connection Error"

def setup_ssh():
    print(f"{yellow}[+] Configuring SSH Environment...")
    os.system("sudo mkdir -p /.ssh")
    # GitHub ကနေ Key တွေယူမယ်
    pub_url = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine.pub"
    prv_url = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine"
    
    os.system(f"sudo wget -q {pub_url} -O /.ssh/google_compute_engine.pub")
    os.system(f"sudo wget -q {prv_url} -O /.ssh/google_compute_engine")
    os.system("sudo chmod 600 /.ssh/google_compute_engine")
    
    # User iam404 ဆောက်မယ်
    username = "iam404"
    password = "12345"
    os.system(f"sudo useradd -m -p {password} {username} 2>/dev/null")
    os.system(f'echo "{username}:{password}" | sudo chpasswd')
    print(f"{green}[√] SSH Setup Completed.")

def get_cloud_ip():
    try:
        r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run'], stdout=subprocess.PIPE)
        output = r.stdout.decode()
        # Extracting IP from dry-run string
        ip = output.split('@')[1].split()[0]
        return ip
    except:
        return None

def main():
    os.system("clear")
    print(logo)
    
    # Stay Alive Background Thread ကို စတင်မယ်
    threading.Thread(target=stay_alive_loop, daemon=True).start()
    
    setup_ssh()
    ip = get_cloud_ip()
    
    if ip:
        print(f"{yellow}[+] Updating Dynamic DNS (Dynv6)...")
        status = duckdns_update(ip)
        
        print(f"\n{green} ◈─────⪧ SSH ACCOUNT INFO ⪦─────◈ ")
        print(f"{cyan} Host / IP   : {white}{ip}")
        print(f"{cyan} SSH Port    : {white}6000")
        print(f"{cyan} Username    : {white}iam404")
        print(f"{cyan} DNS Status  : {white}{status}")
        print(f"{green} ◈──────⪧ S M A R T - 4 0 4 ⪦──────◈ \n")
        
        print(f"{yellow}[!] Tool is now in Stay-Alive mode.")
        print(f"{yellow}[!] Please keep this tab open and use 'tmux' for background running.")
    else:
        print(f"{red}[!] Error: Could not retrieve Cloud Shell IP.")

    # အဆုံးမရှိ စောင့်နေအောင် လုပ်ထားခြင်း
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{red}[!] Stopped by user.")
        sys.exit()
