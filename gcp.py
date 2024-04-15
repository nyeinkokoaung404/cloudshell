import subprocess
import sys
import wget
import os.path
import requests

def duckdns_update(domains, token, ip, verbose=False):
    """Update duckdns.org Dynamic DNS record.

    Args:
        domains (str): The DuckDNS domains to update as comma separated list.
        token (str): An UUID4 provided by DuckDNS for your user.
        verbose (bool): Returns info about whether or not IP has been changed as
            well as if the request was accepted.

    Returns:
        "OK" or "KO" depending on success or failure. Verbose adds IP and change
        status as well.

    """
    params = {
        "domains": domains,
        "token": token,
        "ip": ip,
        "verbose": verbose
    }
    r = requests.get("https://www.duckdns.org/update", params)
    return r.text.strip().replace('\n', ' ')
token = "4f0bc9a7-58b7-465f-91e8-6a1211393788"
domain = "nyeinkokoaung.duckdns.org"

def download_key():
    url_pub = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine.pub"
    url_prv = "https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine"
    pub = '/.ssh/google_compute_engine.pub'
    prv = '/.ssh/google_compute_engine'
    loc = '/.ssh'

    if os.path.exists(pub):
        os.remove(pub)
    if os.path.exists(prv):
        os.remove(prv)
    try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine.pub' ])  
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine' ])     
    except:
         print(f"Failed to add user.")                    
         sys.exit(1)
    
    try:
        down = subprocess.run(['sudo', 'wget', 'https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine.pub']) 
        down2 = subprocess.run(['sudo', 'wget', 'https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/main/google_compute_engine' ]) 
    except:
        pass
    subprocess.run(['sudo', 'mv', 'google_compute_engine.pub', '.ssh/' ])
    subprocess.run(['sudo', 'mv', 'google_compute_engine', '.ssh/' ])
# add user function
def add_user():
 
     # Ask for the input
     username = "nyeinkoko"
 
     # Asking for users password
     password = "nyeinkoko"
        
     try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'useradd', '-p', password, username ])
         # subprocess.run(['sudo', 'chpasswd', '-m', username, password ])
     except:
         print(f"Failed to add user.")                    
         sys.exit(1)



def run_first():
        
     try:
         # executing useradd command using subprocess module
         r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run' ],stdout=subprocess.PIPE)   
         a = r.stdout
         return a
         print('Mods Done')
     except:
         print(f"Failed to create session.")                    
         sys.exit(1)


def run_wget():
        
     try:
         # executing useradd command using subprocess module
         subprocess.run(['pip3', 'install', 'wget'])
         print('Installing....Wget Moldule Done✅')
         
     except:
         print(f"Wget Already Installed.🦋")                    
         sys.exit(1)

try:
    add_user()
except:
    pass


run_wget()


run_first()


download_key()

res = run_first()
re = res.decode()
#words, ss = re.split('=no ')


#try:
    #ips, ssss = ss.split(' -- PROJECT_ID')
    #user,ip = ips.split('@')

    #print("Here is Current INFO")

    #print(ip + " <<< Host : Port >>> 6000")

    #print("nkka404")
    #duckdns_update(domain, token, ip)
#except:
      #ips, ssss = ss.split(' --')
      #user,ip = ips.split('@')

#print(" ◈─────⪧ SSH ACCOUNT ⪦─────◈ ")

#print(" Host / IP   :⪧  " + ip)
#print(" SSH Port    :⪧  6000")
#print(" Username    :⪧  " + user)
#duckdns_update(domain, token, ip)
#print(" ")

#print(" AUTO UPDATE IP TO DUCKDNS--DONE..✅")

#print(" ◈─────⪧ SSH ACCOUNT ⪦─────◈")

#print(" Host / IP   :⪧  nyeinkokoaung404.duckdns.org")
#print(" SSH Port    :⪧  6000")
#print(" Username    :⪧  nyeinkoko")
#print(" ")
#print(" Use Private Key to access server🔻🔻")
#print(" ")
#print(" 💠 💠 💠 Private Key 💠 💠 💠")
#print(" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ")
#print("https://raw.githubusercontent.com/NyeinKoKoAung/CloudShell/main/google_compute_engine")
#print(" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ")
#print(" ")
#print(" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ")
#print("  ___   ___          ________          ___   ___                            ")
#print(" |\  \ |\  \        |\   __  \        |\  \ |\  \                           ")
#print(" \ \  \/_\  \       \ \  \|\  \       \ \  \/_\  \                          ")
#print("  \ \______  \       \ \  \/\  \       \ \______  \                         ")
#print("   \|_____|\  \       \ \  \/\  \       \|_____|\  \                        ")
#print("          \ \__\       \ \_______\             \ \__\                       ")
#print("           \|__|        \|_______|              \|__|                       ")
#print(" Contact the developer https://t.me/nkka404 for more information            ")
#print(" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ")
#print (" FREE GCP By Four Zero Four 😎")
#print (" Credit to ModsBots 🌺")
print(" ")
