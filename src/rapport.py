"""Genere un rapport de statistiques."""

from src.stats import moyenne, variance


def rapport(valeurs):
    return f"moyenne={moyenne(valeurs):.2f} variance={variance(valeurs):.2f}"
