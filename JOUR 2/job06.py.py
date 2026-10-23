# Demander le nombre N à l'utilisateur
N = int(input("Entrez un nombre entier N : "))

# Initialiser le compteur
i = 1

# Boucle while pour afficher les N premiers résultats
while i <= N:
    print(f"{i} x 7 = {i * 7}")
    i += 1