# Définition de la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation du produit à 1 (neutre pour la multiplication)
produit = 1

# Variable pour vérifier si au moins un nombre respecte la condition
au_moins_un = False

# Parcours des éléments de la liste
for nombre in L:
    # On vérifie si le nombre est compris entre 25 et 90 inclus
    if 25 <= nombre <= 90:
        produit *= nombre
        au_moins_un = True

# Affichage du résultat
if au_moins_un:
    print("Le produit des valeurs comprises dans [25, 90] est :", produit)
else:
    print("Aucune valeur de la liste n'est dans l'intervalle [25, 90].")