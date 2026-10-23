def distance_gardien(marches, hauteur_cm):
    # 5 voyages par jour, aller-retour (x2), sur 7 jours
    # Résultat converti en mètres (divisé par 100)
    distance_cm = marches * hauteur_cm * 5 * 2 * 7
    distance_m = distance_cm / 100
    print(f"Pour {marches} marches de {hauteur_cm} cm, le gardien parcourt {distance_m:.2f} m par semaine.")

# Test de la commande :
distance_gardien(50, 20)