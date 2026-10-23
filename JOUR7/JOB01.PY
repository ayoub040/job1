def draw_rectangle(width, height):
    # On dessine la ligne du haut
    print("+" + "-" * (width - 2) + "+")
    
    # On dessine les lignes du milieu
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")
        
    # On dessine la ligne du bas
    if height > 1:
        print("+" + "-" * (width - 2) + "+")

# Test de la commande :
draw_rectangle(10, 3)