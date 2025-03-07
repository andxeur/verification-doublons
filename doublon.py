# methode 1
def verification_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
        else:
            return True

    return False


# methode 2
def verification_doublons2(liste):
    return len(liste) != len(set(liste))


# methode 3
def verification_doublons3(liste):
    compteur = {}
    for element in liste:
        if element in compteur:
            return True
        else:
            compteur[element] = 1
    return False


print(verification_doublons([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(verification_doublons2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(verification_doublons3([1, 2,2, 3, 4, 5, 6, 7, 8, 9, 10]))
