import os
import requests
import zipfile
import shutil
from get_infos import get_studio_latest_version

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

def download_and_unzip_github_release():
    print("")
    print("Il semble que vous utilisiez une ancienne version de STUdio.")
    print("Nous vous recommandons FORTEMENT de mettre à jour STUdio pour résoudre les problèmes que vous rencontrez.")
    print("STUdio va s'installer automatiquement pour vous.")
    print("")
    os.system('pause')
    version = get_studio_latest_version()
    if "Erreur" in version:
        return  # Arrêter l'exécution si une erreur s'est produite lors de la récupération de la version
    
    url = f"https://github.com/DantSu/studio/releases/download/{version}/studio-web-ui-{version}-dist.zip"
    local_filename = f"studio-web-ui-{version}-dist.zip"

    # Fonction pour afficher une animation de pourcentage
    def display_progress(progress, total):
        percent = int(progress / total * 100)
        bar = f"{percent}% [{'#' * (percent // 2)}{' ' * (50 - percent // 2)}]"
        print(f"\r{bar}", end='')

    # Téléchargement du fichier avec affichage de la progression
    with requests.get(url, stream=True) as response:
        if response.status_code == 200:
            total_length = response.headers.get('content-length')
            if total_length is None:  # Pas de contenu
                print("Erreur : Contenu introuvable.")
                return
            
            total_length = int(total_length)
            downloaded = 0
            
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    downloaded += len(chunk)
                    f.write(chunk)
                    display_progress(downloaded, total_length)
            
            print(f"\nTéléchargement terminé : {local_filename}")
        else:
            print(f"Erreur de téléchargement : {response.status_code}")
            return

    # Décompression du fichier ZIP avec affichage de la progression
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        extract_dir = f"studio-web-ui-{version}"
        zip_ref.extractall(extract_dir)
        
        total_files = len(zip_ref.infolist())
        for i, file in enumerate(zip_ref.infolist()):
            display_progress(i + 1, total_files)
        
        print(f"\nDécompression terminée : {extract_dir}")

    # Déplacer les fichiers du sous-dossier vers le dossier parent et supprimer le sous-dossier
    inner_dir = os.path.join(extract_dir, os.listdir(extract_dir)[0])
    for filename in os.listdir(inner_dir):
        shutil.move(os.path.join(inner_dir, filename), extract_dir)
    
    os.rmdir(inner_dir)
    print(f"Dossier imbriqué supprimé : {inner_dir}")

    # Suppression du fichier ZIP après extraction
    os.remove(local_filename)
    print(f"Fichier ZIP supprimé : {local_filename}")

