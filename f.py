def compter_occurrences_mots(liste_mots):
    # Créer un dictionnaire vide pour stocker les occurrences
    occurrences = {}

    # Parcourir la liste de mots
    for mot in liste_mots:
        # Si le mot est déjà une clé dans le dictionnaire, augmenter le compteur
        if mot in occurrences:
            occurrences[mot] += 1
        # Sinon, ajouter le mot au dictionnaire avec une occurrence initiale de 1
        else:
            occurrences[mot] = 1

    return occurrences

# Exemple d'utilisation de la fonction
liste_mots = ["chat", "chien", "chat", "oiseau", "chien", "chat"]
resultat = compter_occurrences_mots(liste_mots)
print(resultat)
