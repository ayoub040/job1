def moyenne(note1, note2, note3):
    # Calcule et retourne la moyenne des trois notes
    return (note1 + note2 + note3) / 3


# Demander à l'utilisateur de saisir trois notes (en convertissant en float pour accepter les décimaux)
n1 = float(input("Entrez la première note : "))
n2 = float(input("Entrez la deuxième note : "))
n3 = float(input("Entrez la troisième note : "))

# Enregistrer le résultat dans la variable « moyenne_etudiant »
moyenne_etudiant = moyenne(n1, n2, n3)

# Afficher la moyenne (optionnel mais pratique pour vérifier)
print(f"Votre moyenne est de : {moyenne_etudiant}")

# Afficher l'appréciation en fonction de la moyenne
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("Moyenne invalide")