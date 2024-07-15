from downloader import download_and_unzip_github_release
import requests
import os
import zipfile
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_studio_update():
    # Check if the studio is up to date from GitHub
    # If not, update the studio by suppressing every old files and downloading the new version
    
    # Get the latest version of STUdio from GitHub
    try:
        response = requests.get("https://api.github.com/repos/DantSu/studio/releases/latest")
        response.raise_for_status()
        version = response.json()["tag_name"].replace("STUdio v", "")
    except requests.RequestException:
        print("Erreur lors de la récupération de la version de STUdio.\n"
              "Veuillez vérifier votre connexion Internet ou désactiver votre VPN et réessayer.")
        return "Erreur lors de la récupération de la version de STUdio."
    
    # Check if the local version is the latest
    if os.path.exists(f"studio-web-ui-{version}.jar"):
        return f"Up to date: DantSu STUdio {version}\n"
    
    # If not, download the new version
    download_and_unzip_github_release()
    return f"Updated: DantSu STUdio {version}\n"