# Importation des modules
import os
import platform
import subprocess
import requests
import webbrowser
import zipfile
from get_infos import get_system_info, get_java_info, get_studio_latest_log, get_studio_local_version, get_studio_latest_version
from downloader import download_and_unzip_github_release

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

print(f"{bcolors.WARNING}WARNING : CE PROGRAMME EST EN COURS DE DÉVELOPPEMENT ET PEUT NE PAS FONCTIONNER CORRECTEMENT.{bcolors.ENDC}")

# Fonction pour créer le fichier contenant les informations
def create_info_file():
    with open("full-log.txt", "w") as file:
        file.write(get_system_info())
        file.write("==============================\n")
        file.write(get_java_info())
        file.write("==============================\n")
        file.write(get_studio_local_version())
        file.write("==============================\n")
        file.write(get_studio_latest_log())


def logger():
    print("Ce programme va récupérer des informations sur différentes informations afin de mieux vous aider.")
    print("Ces informations serons collectées : Version de Java, Information du système d'exploitation, version de STUdio et le fichier studio-latest.log.")
    print("Voulez-vous continuer? (Y/N)")
    print("")
    user_input = input()
    if user_input.lower() == "y":
        try:
            create_info_file()
            print("")
            print("\033[92m" + "Nous avons récupéré les informations avec succès. Les informations ont été stockées dans le fichier full-log.txt.")
            print("Veuillez envoyer ce fichier sur discord pour obtenir de l'aide.")
            os.system('pause')
            exit()
        except Exception as e:
            print("Erreur: " + str(e))
            print(f"{bcolors.FAIL}Une erreur s'est produite lors de la récupération des informations.{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Veuillez suivre les instructions ci-dessous pour résoudre le problème:{bcolors.ENDC}")
            print(f"{bcolors.FAIL}1. Assurez-vous que vous avez les permissions nécessaires pour accéder aux fichiers et dossiers. Si vous êtes sur Windows, exécutez le programme en tant qu'administrateur.{bcolors.ENDC}")
            print(f"{bcolors.FAIL}2. Assurez-vous que le fichier studio-latest.log est présent dans le même répertoire que le programme{bcolors.ENDC}")
            print(f"{bcolors.FAIL}3. Assurez-vous que Java est installé et configuré correctement sur votre système.{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Si vous rencontrez toujours des problèmes, veuillez contacter un modérateur pour obtenir de l'aide.{bcolors.ENDC}")
    else:
        print("Le programme va se fermer...")

def solver():
    print("")
    print("Il semble que vous ayez un problème avec STUdio.")
    print("Je suis là pour vous aider !")
    print("")
    print("Pour commencer, j'ai besoin de quelques informations sur votre système d'exploitation et votre compte utilisateur afin de mieux comprendre le problème.")
    print("Ces informations ne quittent pas votre ordinateur")
    print("Voulez-vous continuer? (Y/N)")
    print("")

    user_input = input()
    if user_input.lower() == "y":
        print("")
        print("Je vais maintenant vérifier si vous utilisez la dernière version de STUdio.")
        if get_studio_local_version() == "DantSu STUdio " + get_studio_latest_version() + "\n":
            print("\033[92m" + "Vous semblez utiliser la dernière version de STUdio.")
        else:
            download_and_unzip_github_release()
            print("")
            print(f"{bcolors.OKGREEN}STUdio a été mis à jour avec succès !{bcolors.ENDC}")
            print(f"{bcolors.WARNING}Cependant, le travail n'est pas encore fini !")
            print(f"Veuillez fermer ce programme et le deplacer dans le dossier contenant la nouvelle version de STUdio.")
            print(f"Le dossier contenant la nouvelle version de STUdio est nommé studio-web-ui-{get_studio_latest_version()}.")
            print(f"Ensuite, exécutez à nouveau ce programme pour obtenir de l'aide.{bcolors.ENDC}")
            os.system('pause')
            print("")
            exit()
        

        print("Je vais vérifier si Java est installé et configuré correctement sur votre système.")
        if "Erreur" in get_java_info():
            print(f"{bcolors.FAIL}Il semble que Java ne soit pas installé ou configuré correctement.{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Veuillez installer Java et assurez-vous qu'il est configuré correctement.{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Vous pouvez télécharger Java à partir du site officiel: https://www.oracle.com/java/technologies/downloads/{bcolors.ENDC}")
        else:
            print("")
            print(f"{bcolors.OKGREEN}Java semble correctement installé sur votre ordinateur{bcolors.ENDC}")
            print("")

        os.system('pause')


        print("Je vous conseille de demander de l'aide à un modérateur pour résoudre votre problème.")
        print("Voulez-vous que je récupère les informations nécessaires pour vous afin de faciliter l'aide apportée par un modérateur? (Y/N)")
        print("")
        user_input = input()
        if user_input.lower() == "y":
            logger()
        else:
            print("Je n'ai pas pu trouver de solution à votre problème...")
            print("Veuillez contacter un modérateur pour obtenir de l'aide.")
            print("Il est cependement FORTEMENT recommandé de récupérer les informations nécessaires pour faciliter l'aide apportée par un modérateur.")
            print("Le programme va se fermer...")
            exit()
    else:
        print("Le programme va se fermer... Aucune information n'a été collectée.")
        exit()



def main():
    print("Bienvenue dans le programme de récupération d'informations sur STUdio.")
    print("Veuillez choisir l'option qui correspond à votre situation:")
    print("1. Vous avez un problème avec STUdio et vous avez besoin d'aide.")
    print("2. Un modérateur vous a demandé de récupérer le fichier log pour obtenir de l'aide.")
    print("3. Quitter le programme.")
    print("")

    user_input = input()
    if user_input == "1":
        solver()
    elif user_input == "2":
        logger()
    elif user_input == "3":
        print("Le programme va se fermer...")
        os.system('pause')
        exit()
    else:
        print("Veuillez choisir une option valide.")
        main()

if __name__ == "__main__":
    main()
