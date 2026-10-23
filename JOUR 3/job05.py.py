# On parcourt les nombres de 2 à 1000 inclus (1 n'est pas un nombre premier)
for n in range(2, 1001):
    est_premier = True
    
    # On teste si n a un diviseur autre que 1 et lui-même
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            est_premier = False
            break
            
    # Si aucun diviseur n'a été trouvé, c'est un nombre premier
    if est_premier:
        print(n)