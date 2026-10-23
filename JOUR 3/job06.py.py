# Demander un nombre à l'utilisateur (converti en entier)
nombre = int(input("Entrez un nombre : "))

# Vérifier si le nombre est pair ou impair
if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair")
else:
    print(f"Le nombre {nombre} est impair")