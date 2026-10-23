# On parcourt les nombres de 1 à 100 inclus
for i in range(1, 101):
    # Si le nombre est multiple de 3 ET de 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Si le nombre est seulement multiple de 3
    elif i % 3 == 0:
        print("Fizz")
    # Si le nombre est seulement multiple de 5
    elif i % 5 == 0:
        print("Buzz")
    # Sinon, on affiche le nombre
    else:
        print(i)