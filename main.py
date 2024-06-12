# Importation des modules
import os
import platform
import subprocess
import requests
import webbrowser
import zipfile
from get_infos import get_system_info, get_java_info, get_studio_latest_log, get_studio_local_version, get_studio_latest_version
from downloader import download_and_unzip_github_release

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
            print("Nous avons récupéré les informations avec succès. Les informations ont été stockées dans le fichier full-log.txt.")
            print("Veuillez envoyer ce fichier sur discord pour obtenir de l'aide.")
            os.system('pause')
            exit()
        except Exception as e:
            print("Erreur: " + str(e))
            print("Une erreur s'est produite lors de la récupération des informations.")
            print("Veuillez suivre les instructions ci-dessous pour résoudre le problème:")
            print("1. Assurez-vous que vous avez les permissions nécessaires pour accéder aux fichiers et dossiers. Si vous êtes sur Windows, exécutez le programme en tant qu'administrateur.")
            print("2. Assurez-vous que le fichier studio-latest.log est présent dans le même répertoire que le programme")
            print("3. Assurez-vous que Java est installé et configuré correctement sur votre système.")
            print("Si vous rencontrez toujours des problèmes, veuillez contacter un modérateur pour obtenir de l'aide.")
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
            print("Vous semblez utiliser la dernière version de STUdio.")
        else:
            print("")
            print("Il semble que vous utilisiez une ancienne version de STUdio.")
            print("Nous vous recommandons FORTEMENT de mettre à jour STUdio pour résoudre les problèmes que vous rencontrez.")
            print("STUdio va s'installer automatiquement pour vous. Voulez-vous continuer? (Y/N)")
            print("")
            os.system('pause')
            download_and_unzip_github_release()
            os.system('pause')
            print("")
            print("STUdio a été installé avec succès. Veuillez redémarrer STUdio pour appliquer les changements.")
            os.system('pause')
    else:
        print("Le programme va se fermer... Aucune information n'a été collectée.")



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
