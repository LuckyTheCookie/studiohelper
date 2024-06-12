# get_infos.py

import os
import platform
import subprocess
import requests

def get_system_info():
    return (f"System Information\n"
            f"OS: {platform.system()} {platform.release()}\n"
            f"Version: {platform.version()}\n"
            f"Architecture: {platform.architecture()[0]}\n"
            f"Machine: {platform.machine()}\n"
            f"Processor: {platform.processor()}\n")

def get_java_info():
    return "Java Information\n" + subprocess.run(["java", "-version"], capture_output=True, text=True).stderr

def get_studio_latest_log():
    try:
        with open("studio-latest.log", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Le fichier studio-latest.log n'a pas été trouvé.\n"
              "Veuillez placer ce programme dans le dossier STUdio et exécuter le programme s'il vous plait\n"
              "Le programme va se fermer...")

def get_studio_latest_version():
    try:
        response = requests.get("https://api.github.com/repos/DantSu/studio/releases/latest")
        response.raise_for_status()
        return response.json()["tag_name"].replace("STUdio v", "")
    except requests.RequestException:
        print("Erreur lors de la récupération de la version de STUdio.\n"
              "Veuillez vérifier votre connexion Internet ou désactiver votre VPN et réessayer.")
        return "Erreur lors de la récupération de la version de STUdio."

def get_studio_local_version():
    version = get_studio_latest_version()
    if os.path.exists(f"studio-web-ui-{version}.jar"):
        return f"DantSu STUdio {version}\n"
    return "Ancienne version de STUdio ou Version introuvable\n"
