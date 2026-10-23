# Demander les trois longueurs à l'utilisateur (converties en float pour accepter les décimaux)
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# 1. Vérifier si on peut construire un triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Ces longueurs permettent de former un triangle.")
    
    # On trie les côtés pour identifier facilement le plus grand (qui sera c_max)
    cotes = sorted([a, b, c])
    x, y, z = cotes[0], cotes[1], cotes[2] # z est le plus grand (hypoténuse potentielle)
    
    # 2. Vérifier les spécificités du triangle
    # Équilatéral (tous les côtés égaux)
    if a == b == c:
        print("Ce triangle est équilatéral.")
    else:
        # Vérification s'il est rectangle (Pythagore : z² = x² + y²)
        # On utilise une petite tolérance (arrondi) pour éviter les soucis de virgule flottante
        est_rectangle = round(z**2, 2) == round(x**2 + y**2, 2)
        
        # Vérification s'il est isocèle (deux côtés égaux)
        est_isocele = (a == b) or (b == c) or (a == c)
        
        # Affichage des résultats selon les cas
        if est_rectangle and est_isocele:
            print("Ce triangle est rectangle et isocèle.")
        elif est_rectangle:
            print("Ce triangle est rectangle.")
        elif est_isocele:
            print("Ce triangle est isocèle.")
        else:
            print("Ce triangle est quelconque.")
else:
    print("Impossible de construire un triangle avec ces longueurs.")