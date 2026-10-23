def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur non valide"


# Tests du programme avec différents opérateurs
print(calcule(10, "+", 5))  # Affiche 15
print(calcule(20, "-", 8))  # Affiche 12
print(calcule(6, "*", 7))  # Affiche 42
print(calcule(10, "/", 2))  # Affiche 5.0
print(calcule(10, "%", 3))  # Affiche 1