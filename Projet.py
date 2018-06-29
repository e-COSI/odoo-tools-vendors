import git
import json
import click

with open('testjson.json') as json_file:  
    data = json.load(json_file)
    addonsacloner=input("Saisissez l'adresse de l'addons à cloner :")
    trouver=False
    if trouver==False:
        for addons in data["addons"]:
            if addonsacloner==addons["repo"]:
                branche=input("Saisissez la branche de l'addons à cloner (Saisir aucune si la version, de la branche de l'addons,la plus récente à cloner):")
                if branche=="aucune":
                    git.Repo.clone_from(addons["repo"],"ProjetTest")
                    print("Addons cloné")
                else:
                    technical_name=input("Saisissez le dossier à cloner (Saisir aucun si tout la branche à cloner):")
                    if technical_name=="aucun":
                        test=git.Repo.clone_from(addons["repo"],"BrancheTest")
                        test.git.checkout(branche)
                        print("La branche a bien été clonée")
                    else:
                        test=git.Repo.clone_from(addons["repo"],"DossierTest")
                        test.git.checkout(branche)
                        """A completer"""
                        print("Le dossier a bien été cloné")
                trouver=True
    if trouver==False:
        print("L'addons n'existe pas dans le fichier JSON")