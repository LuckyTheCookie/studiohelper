import os
from get_infos import (
    get_system_info,
    get_java_info,
    get_studio_latest_log,
    get_studio_local_version,
    get_studio_latest_version,
)
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
    print("\nCe programme va récupérer des informations sur différentes informations afin de mieux vous aider.\n"
          "Ces informations serons collectées : Version de Java, Information du système d'exploitation, version de STUdio et le fichier studio-latest.log.\n"
          "Voulez-vous continuer? (Y/N)\n")
    if input().strip().lower() == "y":
        try:
            create_info_file()
            print(f"\n{bcolors.OKGREEN}Nous avons récupéré les informations avec succès. Les informations ont été stockées dans le fichier full-log.txt.\n"
                  "Veuillez envoyer ce fichier sur discord pour obtenir de l'aide.")
            os.system("clip < full-log.txt")
            print(f"{bcolors.OKCYAN}Le fichier a été copié dans le presse-papiers, vous pouvez le coller directement dans discord.")
            os.system('pause')
        except Exception as e:
            print(f"{bcolors.FAIL}Une erreur s'est produite lors de la récupération des informations: {str(e)}\n"
                  "1. Assurez-vous que vous avez les permissions nécessaires pour accéder aux fichiers et dossiers. "
                  "Si vous êtes sur Windows, exécutez le programme en tant qu'administrateur.\n"
                  "2. Assurez-vous que le fichier studio-latest.log est présent dans le même répertoire que le programme.\n"
                  "3. Assurez-vous que Java est installé et configuré correctement sur votre système.\n"
                  "Si vous rencontrez toujours des problèmes, veuillez contacter un modérateur pour obtenir de l'aide.")
    else:
        print("Le programme va se fermer...")

def solver():
    print("\nIl semble que vous ayez un problème avec STUdio. Je suis là pour vous aider !\n"
          "Pour commencer, j'ai besoin de quelques informations sur votre système d'exploitation et votre compte utilisateur afin de mieux comprendre le problème.\n"
          "Ces informations ne quittent pas votre ordinateur\nVoulez-vous continuer? (Y/N)\n")
    if input().strip().lower() == "y":
        if get_studio_local_version() == f"DantSu STUdio {get_studio_latest_version()}\n":
            print(f"{bcolors.OKGREEN}Vous semblez utiliser la dernière version de STUdio.")
        else:
            download_and_unzip_github_release()
            print(f"{bcolors.OKGREEN}STUdio a été mis à jour avec succès !\n"
                  f"{bcolors.WARNING}Veuillez fermer ce programme et le déplacer dans le dossier contenant la nouvelle version de STUdio.\n"
                  f"Le dossier contenant la nouvelle version de STUdio est nommé studio-web-ui-{get_studio_latest_version()}.\n"
                  "Ensuite, exécutez à nouveau ce programme pour obtenir de l'aide.")
            os.system('pause')
            exit()

        if "Erreur" in get_java_info():
            print(f"{bcolors.FAIL}Il semble que Java ne soit pas installé ou configuré correctement.\n"
                  "Veuillez installer Java et assurez-vous qu'il est configuré correctement.\n"
                  "Vous pouvez télécharger Java à partir du site officiel: https://www.oracle.com/java/technologies/downloads/")
        else:
            print(f"{bcolors.OKGREEN}Java semble correctement installé sur votre ordinateur{bcolors.ENDC}\n")
        os.system('pause')

        print("Voulez-vous que je récupère les informations nécessaires pour vous afin de faciliter l'aide apportée par un modérateur? (Y/N)\n")
        if input().strip().lower() == "y":
            logger()
        else:
            print("Veuillez contacter un modérateur pour obtenir de l'aide.\n"
                  "Le programme va se fermer...")
            exit()
    else:
        print("Le programme va se fermer... Aucune information n'a été collectée.")
        exit()

def main():
    print("Bienvenue dans le programme de récupération d'informations sur STUdio.\n"
          "Veuillez choisir l'option qui correspond à votre situation:\n"
          "1. Vous avez un problème avec STUdio et vous avez besoin d'aide.\n"
          "2. Un modérateur vous a demandé de récupérer le fichier log pour obtenir de l'aide.\n"
          "3. Quitter le programme.\n")
    user_input = input().strip()
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
