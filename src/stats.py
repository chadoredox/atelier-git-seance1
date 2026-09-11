"""Statistiques descriptives."""


def somme(valeurs):
    total = 0
    for v in valeurs:
        total += v
    return total


def moyenne(valeurs):
    return somme(valeurs) / len(valeurs)
