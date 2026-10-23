def time_to_text(minutes):
    # Calcul des heures (division entière par 60)
    heures = minutes // 60
    # Calcul des minutes restantes (le reste de la division par 60)
    minutes_restantes = minutes % 60

    # Affichage du résultat sous la forme demandée
    print(f"{heures} heures et {minutes_restantes} minutes")


# Tests du programme avec différentes valeurs de minutes
time_to_text(90)   # Affiche "1 heures et 30 minutes"
time_to_text(125)  # Affiche "2 heures et 5 minutes"
time_to_text(45)   # Affiche "0 heures et 45 minutes"
time_to_text(360)  # Affiche "6 heures et 0 minutes"