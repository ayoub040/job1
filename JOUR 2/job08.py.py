# On initialise la valeur de départ à 0 (ou on commence à multiplier)
valeur = 0

# Boucle de 1 à 12 tours
for tour in range(1, 13):
    valeur += 2
    print(f"Tour {tour}: {valeur}")