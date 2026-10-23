# Boucle de 0 à 100 inclus (donc 101 comme borne de fin)
for i in range(101):
    # On vérifie si le nombre n'est PAS 26, 37 ou 88
    if i != 26 and i != 37 and i != 88:
        print(i)