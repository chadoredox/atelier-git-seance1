"""Configuration de l'application."""

import os

APP_NAME = "Atelier Git"
# Resolution du conflit (feature/configuration vs fix/configuration) :
# les deux branches modifiaient la meme ligne APP_API_URL. Choix combine :
# prod par defaut, staging surchargeable via la variable d'environnement.
APP_API_URL = os.environ.get("APP_API_URL", "https://api.intechinfo.fr/v1")
