"""Test de non-regression pour le rapport de statistiques (bisect).

Retourne 0 si le calcul est correct, 1 sinon. Un commit sans
src/rapport.py est considere comme bon (le module n'existe pas encore).
"""
import os
import sys

if not os.path.exists("src/rapport.py"):
    print("src/rapport.py absent -> commit bon")
    sys.exit(0)

sys.path.insert(0, os.getcwd())
from src.rapport import rapport

sortie = rapport([1, 2, 3, 4])
# variance de population de [1, 2, 3, 4] = 1.25
if "variance=1.25" not in sortie:
    print(f"ECHEC: sortie incorrecte -> {sortie}")
    sys.exit(1)
print(f"OK -> {sortie}")
sys.exit(0)
