# downloader.py

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

def display_progress(progress, total):
    percent = int(progress / total * 100)
    bar = f"{percent}% [{'#' * (percent // 2)}{' ' * (50 - percent // 2)}]"
    print(f"\r{bar}", end='')

def download_and_unzip_github_release():
    print("\nIl semble que vous utilisiez une ancienne version de STUdio.\n"
          "Nous vous recommandons FORTEMENT de mettre à jour STUdio pour résoudre les problèmes que vous rencontrez.\n"
          "STUdio va s'installer automatiquement pour vous.\n")
    os.system('pause')

    version = get_studio_latest_version()
    if "Erreur" in version:
        print(f"{bcolors.FAIL}Erreur lors de la récupération de la version de STUdio.{bcolors.ENDC}")
        return

    url = f"https://github.com/DantSu/studio/releases/download/{version}/studio-web-ui-{version}-dist.zip"
    local_filename = f"studio-web-ui-{version}-dist.zip"

    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            total_length = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    downloaded += len(chunk)
                    f.write(chunk)
                    display_progress(downloaded, total_length)

            print(f"\nTéléchargement terminé : {local_filename}")

        with zipfile.ZipFile(local_filename, 'r') as zip_ref:
            extract_dir = f"studio-web-ui-{version}"
            zip_ref.extractall(extract_dir)

            total_files = len(zip_ref.infolist())
            for i, file in enumerate(zip_ref.infolist()):
                display_progress(i + 1, total_files)

            print(f"\nDécompression terminée : {extract_dir}")

        inner_dir = os.path.join(extract_dir, os.listdir(extract_dir)[0])
        for filename in os.listdir(inner_dir):
            shutil.move(os.path.join(inner_dir, filename), extract_dir)

        os.rmdir(inner_dir)
        print(f"Dossier imbriqué supprimé : {inner_dir}")

        for filename in os.listdir(extract_dir):
            shutil.move(os.path.join(extract_dir, filename), os.getcwd())
        shutil.rmtree(extract_dir)

        print(f"[{bcolors.OKGREEN}SUCCESS{bcolors.ENDC}] STUdio a été mis à jour avec succès !\n")
    except requests.RequestException as e:
        print(f"{bcolors.FAIL}Erreur de téléchargement : {e}{bcolors.ENDC}")
    except zipfile.BadZipFile:
        print(f"{bcolors.FAIL}Erreur lors de la décompression du fichier ZIP.{bcolors.ENDC}")
    except Exception as e:
        print(f"{bcolors.FAIL}Une erreur s'est produite : {e}{bcolors.ENDC}")
        print(f"Assurez-vous que ce programme soit éxécuté dans un dossier vide.")
        print(f)
    finally:
        if os.path.exists(local_filename):
            os.remove(local_filename)
            print(f"Fichier ZIP supprimé : {local_filename}")
