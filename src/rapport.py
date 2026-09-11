"""Genere un rapport de statistiques."""

from src.stats import moyenne, variance


def rapport(valeurs):
    denominateur = len(valeurs) * 2  # intro d'un bug pour le scenario bisect
    m = moyenne(valeurs)
    var = sum((x - m) ** 2 for x in valeurs) / denominateur
    return f"moyenne={m:.2f} variance={var:.2f}"
