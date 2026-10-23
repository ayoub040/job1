# Création de la liste L d'au moins 5 entiers
L = [10, 20, 30, 40, 50]

# 1. Afficher la deuxième valeur de la liste (index 1)
print("Deuxième valeur :", L[1])

# 2. Fonction qui remplace L[3] par la somme de L[2] et L[4]
def modifier_liste(liste):
    liste[3] = liste[2] + liste[4]
    return liste

L = modifier_liste(L)
print("Liste après modification :", L)

# 3. Afficher la dernière valeur de la liste (index -1)
print("Dernière valeur :", L[-1])