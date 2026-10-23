# Création de la chaîne de base répétée 10 fois
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# On définit la longueur de la première ligne (et le pas d'augmentation)
largeur = 1
index = 0

# Tant qu'on a assez de caractères dans la chaîne pour faire une ligne complète
while index + largeur <= len(chaine):
    # On extrait et affiche la tranche de caractères correspondante
    print(chaine[index : index + largeur])
    
    # On passe à l'index suivant et on augmente la taille de la ligne de 2
    index += largeur
    largeur += 2