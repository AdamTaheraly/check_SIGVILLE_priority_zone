#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Adam Taheraly
Aim: Request to the SIG API (https://sig.ville.gouv.fr/) if an adress is part of a "Quartier Prioritaire" (QP)
Input: .csv file with adress for each children (
        "Rang", "Titre_referents",
        "Prenom_referents", "Nom_referents",
        "Prenom_enfant", "Nom_enfant",
        "num_voie", "nom_voie", "complement_adresse", "code_postal", "nom_commune"
        )
Output: Input file with API code reponse value about the localization in a "Quartier Prioritaire" for each adress
"""

import requests

# Define core function to request to the API if an adress is part of "Quartier Prioritaire"
def quartier_prioritaire(code_postal, nom_commune, num_voie, nom_voie):
    """
    Send a POST cURL request to the API with data in JSON format.
    Return CODE_REPONSE value from the JSON format reponse of the API. 
    """
    cookies = {
        'BACKENDID': 'vs103.anct',
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic BASE64', # BASE64 = base64-encode(username:password)
        # 'Cookie': 'BACKENDID=vs103.anct',
    }

    json_data = {
        'type_quartier': 'QP',
        'type_adresse': 'WSA',
        'adresse': {
            'code_postal': code_postal,
            'nom_commune': nom_commune,
            'num_voie': num_voie,
            'nom_voie': nom_voie,
        },
    }
    response = requests.post(
        'https://wsa.sig.ville.gouv.fr/service/georeferenceur.json',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    
    return response.json()["code_reponse"]

# Open input and output files
with open("ASI_zone_prioritaire.csv", "r", encoding="utf-8") as data:
    header = (
        "Rang", "Titre_referents",
        "Prenom_referents", "Nom_referents",
        "Prenom_enfant", "Nom_enfant",
        "num_voie", "nom_voie", "complement_adresse", "code_postal", "nom_commune"
    )
    with open("ASI_zone_prioritaire_output.csv", "w", encoding="utf-8") as result:
        row = 0 # Set on/off variable to pass first line of input file
        header_result = ",".join(header) + ",Code_reponse\n"
        result.write(header_result) # Write header of the output file
        for line in data: # Iter through input file, send a post request and write result in output file
            if row != 0:
                child = {title:value for title, value in zip(header, line.split(","))}
                
                if child["num_voie"] and child["nom_voie"] and child["code_postal"] and child["nom_commune"]:
                    QP = quartier_prioritaire(child["code_postal"], child["nom_commune"],
                                          child["num_voie"], child["nom_voie"])
                    result.write(f"{line.strip()},{QP}\n")
                else:
                    result.write(f"{line.strip()},NULL\n")
            else:
                row = 1
