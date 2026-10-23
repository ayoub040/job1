def draw_triangle(height):
    for i in range(height):
        # Affiche les espaces et les côtés du triangle
        espaces_gauche = " " * (height - i - 1)
        if i == height - 1:
            milieu = "_" * (2 * i)
        else:
            milieu = " " * (2 * i)
        print(espaces_gauche + "/" + milieu + "\\")

# Test de la commande (avec une hauteur de 5 par exemple) :
draw_triangle(5)