def verifier_pair_impair(nombre):
    # Vérifie si le nombre est un entier et s'il est positif (ou égal à 0)
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")
    else:
        print(f"Erreur : '{nombre}' n'est pas un nombre entier et positif valide.")


# Tests du programme avec différentes valeurs
verifier_pair_impair(4)  # Nombre pair et positif
verifier_pair_impair(7)  # Nombre impair et positif
verifier_pair_impair(0)  # Zéro (entier positif)
verifier_pair_impair(-3)  # Nombre négatif (génère une erreur)
verifier_pair_impair(5.5)  # Nombre décimal (pas un entier, génère une erreur)