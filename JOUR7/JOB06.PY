def evaluer_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)  # Échec, pas d'arrondi
        else:
            # Vérifie la distance avec le prochain multiple de 5
            reste = note % 5
            if reste >= 3:
                note_arrondie = note + (5 - reste)
                notes_arrondies.append(note_arrondie)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

# Test de la commande :
print(evaluer_notes([83, 82, 38, 48]))