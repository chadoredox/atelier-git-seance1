"""Statistiques descriptives."""


def somme(valeurs):
    total = 0
    for v in valeurs:
        total += v
    return total


def moyenne(valeurs):
    return somme(valeurs) / len(valeurs)


def variance(valeurs):
    m = moyenne(valeurs)
    return sum((x - m) ** 2 for x in valeurs) / len(valeurs)


def ecart_type(valeurs):
    return variance(valeurs) ** 0.5
