# Developer : Nyein Ko Ko Aung (t.me/nkka404)

import subprocess
import sys
import os
import requests
import time
import threading

# Colors
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
    while True:
        current_time = time.ctime()
        print(f"\n{purple}[404-HEARTBEAT]{white} Pulse at {current_time} - Server Active")
        time.sleep(300)

def duckdns_update(ip):
    token = "ykYdgfMLqVhHFkGQSf19ztRhp1WP3J"
    hostname = "nyeinkokoaung.dynv6.net"
    url = f"http://ipv4.dynv6.com/api/update?hostname={hostname}&ipv4={ip}&token={token}"
    try:
        r = requests.get(url, timeout=10)
        return r.text.strip()
    except:
        return "DNS Update Failed"

def setup_ssh():
    print(f"{yellow}[+] Preparing SSH Keys and User...")
    os.system("sudo mkdir -p /.ssh")
    pub_url = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine.pub"
    prv_url = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine"
    
    os.system(f"sudo wget -q {pub_url} -O /.ssh/google_compute_engine.pub")
    os.system(f"sudo wget -q {prv_url} -O /.ssh/google_compute_engine")
    os.system("sudo chmod 600 /.ssh/google_compute_engine")
    
    # System User
    username = "iam404"
    password = "12345"
    os.system(f"sudo useradd -m -p {password} {username} 2>/dev/null")
    os.system(f'echo "{username}:{password}" | sudo chpasswd')
    print(f"{green}[√] SSH Setup Completed.")

def get_ssh_info():
    try:
        r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run'], stdout=subprocess.PIPE)
        res = r.stdout.decode()
        
        ssh_part = res.split('=no ')[1].split(' --')[0]
        user, ip = ssh_part.split('@')
        return user, ip
    except:
        return None, None

def main():
    os.system("clear")
    print(logo)
    
    # Pulse thread
    threading.Thread(target=stay_alive_loop, daemon=True).start()
    
    setup_ssh()
    user, ip = get_ssh_info()
    
    if ip and user:
        print(f"{yellow}[+] Updating Dynv6 IP...")
        dns_status = duckdns_update(ip)
        
        print(f"\n{green} ◈─────⪧ SSH ACCOUNT INFO ⪦─────◈ ")
        print(f"{cyan} Host / IP   :⪧  {white}{ip}")
        print(f"{cyan} SSH Port    :⪧  {white}6000")
        print(f"{cyan} Username    :⪧  {white}{user}")
   #     print(f"{cyan} DNS Update  :⪧  {white}{dns_status}")
        print(f"{green} ◈──────⪧ 4 0 4  S M A R T ⪦──────◈ \n")
        
    #    print(f"{yellow} 💠 Hostname Access: {white}nyeinkokoaung.dynv6.net")
        print(f"{yellow} 💠 Keep this tab open for better stability.")
    else:
        print(f"{red}[!] Error: Could not capture SSH details from gcloud.")

    # Keep script running
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{red}[!] Stopped.")
        sys.exit()
