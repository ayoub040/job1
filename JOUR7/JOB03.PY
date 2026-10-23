def draw_tapis(n):
    for i in range(n + 1):
        ligne = ""
        for j in range(n + 1):
            if j == n - i:
                ligne += " "  # La diagonale vide
            else:
                ligne += "#"
        print(ligne)

# Test de la commande pour une taille de 10 :
draw_tapis(10)