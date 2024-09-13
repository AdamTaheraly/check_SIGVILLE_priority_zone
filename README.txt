version of 13-09-2024
Author: Adam Taheraly
Contact: taheraly.adam@gmail.com

Aim: Identitfy if a list of adresses are part of a "Quartier Prioritaire" from the SIG API (https://sig.ville.gouv.fr/).

Input: .csv file with a list of adress (header = TRUE)
Output: .csv file with a list of adress and the code reponse from the API.

prerequisite : module requests (python -m pip install requests)

Steps:
1) Change BASE64 in post_resquest_sigville.py (line 29) by username:password from your account (encoded in base64).
You can use https://www.base64decode.org/ to encode it.
2) Prepare a ASI_zone_prioritaire.csv (separator: ",") with a list of adress 
   (header: Rang, Titre_referents, Prenom_referents, Nom_referents,
            Prenom_enfant, Nom_enfant, num_voie, nom_voie, 
            complement_adresse, code_postal, nom_commune)
3) Double click on post_resquest_sigville.py
4) Open output file : ASI_zone_prioritaire_output.csv
