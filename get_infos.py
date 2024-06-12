import os
import platform
import subprocess
import requests

# Fonction pour récupérer les informations sur le système d'exploitation
def get_system_info():
    system_info = "System Information\n"
    system_info += "OS: " + platform.system() + " " + platform.release() + "\n"
    system_info += "Version: " + platform.version() + "\n"
    system_info += "Architecture: " + platform.architecture()[0] + "\n"
    system_info += "Machine: " + platform.machine() + "\n"
    system_info += "Processor: " + platform.processor() + "\n"
    return system_info


# Fonction pour récupérer les informations sur Java avec subprocess
def get_java_info():
    java_info = "Java Information\n"
    java_info += subprocess.run(["java", "-version"], capture_output=True, text=True).stderr
    return java_info

# Fonction pour récupérer les informations sur le fichier studio-latest.log
def get_studio_latest_log():
    if os.path.exists("studio-latest.log"):
        with open("studio-latest.log", "r") as file:
            studio_latest_info = file.read()
        return studio_latest_info
    else:
        print("Le fichier studio-latest.log n'a pas été trouvé.")
        print("Veuillez placer ce programme dans le dossier STUdio et exécuter le programme s'il vous plait")
        print("Le programme va se fermer...")
        # Appuyez sur une touche pour fermer la fenêtre
        
# Fonction pour récupérer les informations sur la dernière version de STUdio
# Se connecter à internet et vérifier sur github la dernière version de STUdio Dantsu (https://github.com/DantSu/studio/releases)
def get_studio_latest_version():
    url = "https://api.github.com/repos/DantSu/studio/releases/latest"
    response = requests.get(url)
    data = response.json()
    studio_latest_version = data["tag_name"]
    # Si une erreur se produit lors de la récupération de la version : on affiche un message d'erreur
    if studio_latest_version is None:
        print("Erreur lors de la récupération de la version de STUdio.")
        print("Veuillez vérifier votre connexion Internet ou désactiver votre VPN et réessayer.")
        return "Erreur lors de la récupération de la version de STUdio."
    # Formatage de la version pour retirer "STUdio v" devant le numéro de version
    studio_latest_version = studio_latest_version.replace("STUdio v", "")
    return str(studio_latest_version)
    
# Récupérer le numéro de version de studio dans le même répertoire que le programme
def get_studio_local_version():
    # Si le fichier studio-web-ui-[latest-version].jar, on stocke la version dans une variable
    if os.path.exists("studio-web-ui-" + get_studio_latest_version() + ".jar"):
        studio_local_version = "DantSu STUdio " + get_studio_latest_version() + "\n"
        return studio_local_version
    else:
        studio_local_version = "Ancienne version de STUdio ou Version introuvable\n"
        return studio_local_version 

