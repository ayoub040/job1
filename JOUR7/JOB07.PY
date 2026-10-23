def my_sort(liste):
    coups = 0
    n = len(liste)
    echange = True
    
    while echange:
        echange = False
        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                # On échange les deux éléments
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                coups += 1
                echange = True
                
    print(f"Nombre total de coups nécessaires pour trier la liste: {coups}")
    print(f"Liste triée {liste}")
    return liste

# Test de la commande :
my_sort([64, 34, 25, 12, 22, 11, 90])