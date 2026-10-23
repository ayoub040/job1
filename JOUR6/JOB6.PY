def echanger_premier_dernier(liste):
    if len(liste) > 1:
        liste[0], liste[-1] = liste[-1], liste[0]
    return liste

# Exemple d'utilisation :
ma_liste = [10, 20, 30, 40, 50]
echanger_premier_dernier(ma_liste)

print(ma_liste)
# Sortie : [50, 20, 30, 40, 10]