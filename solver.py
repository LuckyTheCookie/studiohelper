from flask import Flask, render_template, request, jsonify
import os
from get_infos import (
    get_system_info,
    get_java_info,
    get_studio_latest_log,
    get_studio_local_version,
    get_studio_latest_version,
)
from downloader import download_and_unzip_github_release
from main import logger

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

class SolverInterruptedException(Exception):
    pass


def solver():
    try:
        print("\nIl semble que vous ayez un problème avec STUdio. Je suis là pour vous aider !\n"
              "Pour commencer, j'ai besoin de quelques informations sur votre système d'exploitation et votre compte utilisateur afin de mieux comprendre le problème.\n"
              "Ces informations ne quittent pas votre ordinateur\nVoulez-vous continuer? (Y/N)\n")
        if input().strip().lower() != "y":
            print(f"{bcolors.FAIL}Aucune information n'a été récoltée. Veuillez rouvrir votre navigateur afin de continuer s'il vous plait{bcolors.ENDC}")
            raise SolverInterruptedException("Solver has been cancelled.")

        if get_studio_local_version() == f"DantSu STUdio {get_studio_latest_version()}\n":
            print(f"{bcolors.OKGREEN}Vous semblez utiliser la dernière version de STUdio.")
        else:
            download_and_unzip_github_release()
            print(f"{bcolors.OKGREEN}STUdio a été mis à jour avec succès !\n"
                  f"{bcolors.WARNING}Veuillez fermer ce programme et le déplacer dans le dossier contenant la nouvelle version de STUdio.\n"
                  f"Le dossier contenant la nouvelle version de STUdio est nommé studio-web-ui-{get_studio_latest_version()}.\n"
                  "Ensuite, exécutez à nouveau ce programme pour obtenir de l'aide.")
            os.system('pause')
            print(f"{bcolors.FAIL}Veuillez rouvrir votre navigateur afin de continuer s'il vous plait{bcolors.ENDC}")
            raise SolverInterruptedException("Solver requires manual intervention. Please restart the program.")

        if 'java version "21' or 'java version "22' or "java 21" or "java 22" in get_java_info():
            print(f"{bcolors.OKGREEN}Java semble correctement installé sur votre ordinateur{bcolors.ENDC}\n")
        else:
            print(f"{bcolors.FAIL}Il semble que Java ne soit pas installé, configuré correctement, ou que vous utilisiez une ancienne version de Java.\n"
                  "Veuillez installer Java et assurez-vous qu'il est configuré correctement.\n"
                  "Vous pouvez télécharger Java en retournant sur votre navigateur ou à partir du site officiel: https://www.oracle.com/java/technologies/downloads/")
            raise SolverInterruptedException("Java is not installed or configured correctly.")            
        
        print(f"{bcolors.FAIL}Veuillez rouvrir votre navigateur afin de continuer s'il vous plait{bcolors.ENDC}")
        return "Solver finished successfully."
    except SolverInterruptedException as e:
        return str(e)
    except Exception as e:
        print(f"{bcolors.FAIL}UNE ERREUR S'EST PRODUITE - Veuillez rouvrir votre navigateur afin de continuer s'il vous plait{bcolors.ENDC}")
        return f"An unexpected error occurred: {str(e)}"
