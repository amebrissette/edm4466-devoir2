# coding : utf-8

# Bonjour Jean-Hugues! Voici mon deuxième devoir qui a été plus complexe que le premier, mais plus agréable à réaliser. 
# Vous trouverez ma démarche justifiée en #commentaires. Bonne lecture! Amélie :-) 

import csv
import json
import requests
# Importation des fichiers nécessaires à la création du .csv

fichier = "lobbying.csv"
# Création du futur fichier.csv

url = "http://jhroy.ca/uqam/lobby.json"
# Url fournie par Jean-Hugues Roy qui use de «pseudo-API»
# print(url) Petit test print pour confirmer que l'url s'ouvre correctement [réussi] 

entetes = {
    "User-Agent": "Amélie Brissette - 5147780087 : requête envoyée dans le cadre du cours de journalisme EDM4466 à l'UQAM", 
    "From": "amelie-brissette@hotmail.com"
} 
# Création d'une carte de visite informatique (pas obligatoire à la réussite du devoir mais c'est éthique)
# print(entetes) Petit test print pour confirmer que l'entêtes s'affiche correctement [réussi] 

req = requests.get(url,headers=entetes)
print(req)

#n = 0
# Création d'un compteur
 
if req.status_code !=200:
    print("Il y a une erreur qui s'est glissée.")
else: 
    lobby = req.json()
    #print(lobby) Tout le script du fichier json s'imprime (finalement!). En inscrivant le code ainsi je comprends mon erreur qui invalidait mes démarches initiales (laissées en commentaires ci-dessous). 
    
# if req.status_code == 200:
#     print("Bravo ça fonctionne!")
#     lobby = req.json()
#     print(lobby["fr_client_org_corp_nm"])
# else:
#     print("Il y a une erreur qui s'est glissée.")

for lobbies in lobby["registre"]: 
    infos=[]
    comlog=lobbies[0]["comlog_id"]
    nomfr=lobbies[0]["fr_client_org_corp_nm"]
    nomen=lobbies[0]["en_client_org_corp_nm"]
    date=lobbies[0]["date_comm"]
    objet=lobbies[1][0]["objet"]
    objetautre=lobbies[1][0]["objet_autre"]
    institution=lobbies[2][0]["institution"]

    infos.append(comlog)
    infos.append(nomfr)
    infos.append(nomen)
    infos.append(date)
    infos.append(objet)
    infos.append(objetautre)
    infos.append(institution)
    #print(infos) Les inscriptions sélectionnées dans la boucle ci-haut s'impriment correctement (YES!). 

    if "limat" in objet or "limat" in objetautre:
        print(comlog, nomfr, nomen, date, objet, objetautre, institution)
        # Création du code contenant les inscriptions traitant uniquement du climat. 
 
        lobby = open(fichier,"a")
        registrelobbying = csv.writer(lobby)
        registrelobbying.writerow(infos)
        # Ouverture du fichier csv contenant les inscriptions sélectionnées.

# Voici le résultat de mes précieux essais-erreurs. 
# Je laisse ci-dessous ma démarche antérieure infructueuse de création de boucle "for in" et de "if else" (méthode inspirée des notes prises en classe lors du cours précédent).

# for info in lobbies:
#     infos = []
#     # Création d'une liste qui est vide
#     n += 1 
#     # Afficher les inscriptions numérotées à l'aide du compteur

#     req = requests.get(url,headers=entetes)
#     if req.status_code != 200:
#         print("Il y a une erreur qui s'est glissée")
#     else:
#         lobby = req.json()
#         nomfr = lobby["fr_client_org_corp_nm"]
#         totalA = [lobby["en_client_org_corp_nm"]["client_org_corp_num"]["date_comm"]]
#         totalB = [lobby["objet"]["objet_autre"]]
#         totalC = [lobby["institution"]]
#         print(nomfr, totalA)
#         infos.append(n)
#         infos.append(info)
#         infos.append(nomfr)
#         infos.append(totalA, totalB, totalC)
#         print(infos)
        