def calculer_longueur(liste):
    """Calcule la taille d'une liste sans len()."""
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur


def arrondir_nombre(nombre):
    """
    Arrondit un nombre au plus proche sans utiliser round().
    Exemple : 22.4 -> 22 | 17.50 -> 18
    """
    partie_entiere = int(nombre)
    décimale = nombre - partie_entiere

    if décimale >= 0.5:
        return partie_entiere + 1
    else:
        return partie_entiere


def trier_liste(liste):
    """Trie la liste par ordre croissant (tri à bulles) sans range()."""
    n = calculer_longueur(liste)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            if liste[j] > liste[j + 1]:
                # Échange des éléments
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
            j += 1
        i += 1

    return liste


def traiter_et_trier(liste):
    liste_arrondie = []

    # 1. Arrondi de chaque élément sans append()
    for nombre in liste:
        valeur_arrondie = arrondir_nombre(nombre)
        liste_arrondie += [valeur_arrondie]

    # 2. Tri croissant de la liste
    return trier_liste(liste_arrondie)


# Liste initiale
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Exécution
resultat = traiter_et_trier(L)