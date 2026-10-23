def calculer_longueur(liste):
    """Calcule la longueur d'une liste sans utiliser len()."""
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur


def trier_liste(liste):
    """Trie la liste par ordre croissant sans utiliser de fonction système."""
    n = calculer_longueur(liste)

    # Parcourt de la liste
    for i in range(n):
        for j in range(0, n - i - 1):
            # Si l'élément actuel est plus grand que le suivant, on les échange
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    return liste


# Exemple d'utilisation :
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

print("Liste originale :", L)
trier_liste(L)
print("Liste triée     :", L)