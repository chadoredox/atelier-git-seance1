"""Utilitaires de calcul de moyenne."""


def moyenne(notes):
    """Calcule la moyenne arithmetique d'une liste de notes."""
    return sum(notes) / len(notes)


def moyenne_ponderee(notes, coeffs):
    """Calcule la moyenne ponderee d'une liste de notes."""
    if len(notes) != len(coeffs):
        raise ValueError("notes et coeffs doivent avoir la meme longueur")
    return sum(n * c for n, c in zip(notes, coeffs))


def moyenne_securisee(notes):
    """Moyenne qui ne leve pas d'erreur sur une liste vide."""
    return moyenne(notes) if notes else 0
