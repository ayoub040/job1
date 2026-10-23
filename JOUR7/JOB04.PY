def cesar_cipher(message, decalage):
    resultat = ""
    for char in message:
        if char.isalpha():
            # Détermine si c'est une majuscule ou une minuscule
            code_base = ord('A') if char.isupper() else ord('a')
            # Applique le décalage en boucle sur l'alphabet (26 lettres)
            char_decale = chr((ord(char) - code_base + decalage) % 26 + code_base)
            resultat += char_decale
        else:
            resultat += char
    return resultat

# Test de la commande :
print(cesar_cipher("bonjour", 3))