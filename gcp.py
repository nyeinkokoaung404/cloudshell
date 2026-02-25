# -*- coding: UTF-8 -*-
# 404 SMART TOOL - GCP SSH SETUP
# Developer : Nyein Ko Ko Aung (@nkka404)

import subprocess
import sys
import os
import requests
import time

# Colors
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

# Banner of 404
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

def sprint(sentence, second=0.03):
    for word in sentence + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(second)

def duckdns_update(ip):
    # Dynv6 Update API
    token = "ykYdgfMLqVhHFkGQSf19ztRhp1WP3J"
    hostname = "nyeinkokoaung.dynv6.net"
    url = f"http://ipv4.dynv6.com/api/update?hostname={hostname}&ipv4={ip}&token={token}"
    try:
        r = requests.get(url)
        return r.text.strip()
    except:
        return "Failed to update IP"

def download_key():
    print(f"{yellow}[+] Setting up SSH Keys...")
    # Create SSH directory
    os.system("sudo mkdir -p /.ssh/gcp")
    
    # Download keys from GitHub
    pub_url = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine.pub"
    prv_url = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine"
    
    os.system(f"sudo wget -q {pub_url} -O /.ssh/google_compute_engine.pub")
    os.system(f"sudo wget -q {prv_url} -O /.ssh/google_compute_engine")
    os.system("sudo chmod 600 /.ssh/google_compute_engine")
    print(f"{green}[√] SSH Keys downloaded and configured.")

def add_user():
    username = "iam404"
    password = "12345"
    print(f"{yellow}[+] Creating User: {username}...")
    try:
        # Create user and set password
        subprocess.run(['sudo', 'useradd', '-m', '-p', password, username], stderr=subprocess.DEVNULL)
        os.system(f'echo "{username}:{password}" | sudo chpasswd')
        print(f"{green}[√] User {username} created successfully.")
    except:
        print(f"{red}[!] Failed to add user or user already exists.")

def get_cloud_ip():
    print(f"{yellow}[+] Extracting Cloud Shell IP...")
    try:
        r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run'], stdout=subprocess.PIPE)
        output = r.stdout.decode()
        # Logic to extract IP from dry-run output
        parts = output.split('@')
        if len(parts) > 1:
            ip = parts[1].split()[0]
            return ip
    except Exception as e:
        print(f"{red}[!] Error: {e}")
        return None

def main():
    os.system("clear")
    print(logo)
    
    # Run setup
    add_user()
    download_key()
    
    ip = get_cloud_ip()
    
    if ip:
        print(f"{yellow}[+] Updating DNS...")
        status = duckdns_update(ip)
        
        print(f"\n{green} ◈─────⪧ SSH ACCOUNT INFO ⪦─────◈ ")
        print(f"{cyan} Host / IP   : {white}{ip}")
   #     print(f"{cyan} Hostname    : {white}nyeinkokoaung.dynv6.net")
        print(f"{cyan} SSH Port    : {white}6000")
        print(f"{cyan} Username    : {white}iam404")
        print(f"{cyan} Password    : {white}12345")
        print(f"{green} ◈──────⪧ 4 0 4  S M A R T ⪦──────◈ \n")
        
        print(f"{purple} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ")
        print(f"{white} 💠 Use Private Key to Access Server 💠")
        print(f"{purple} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ")
        print(f"{blue} Key: https://raw.githubusercontent.com/Premium-404/Google-Cloud/main/google_compute_engine")
        print(f"{purple} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
        
    else:
        print(f"{red}[!] Could not retrieve Cloud IP. Please check gcloud auth.")

    print(f"{cyan}Developer: @nkka404 | Date: {time.ctime()}")

if __name__ == '__main__':
    try:
        # Ensure requests is installed
        import requests
    except ImportError:
        os.system("pip3 install requests wget")
        
    main()
