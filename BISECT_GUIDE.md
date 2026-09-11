# 📚 Guide Git Bisect - Exercice Pratique

## Objectif
Trouver le commit qui a introduit un bug dans l'historique en utilisant `git bisect`.

## Scénario
Un bug a été introduit quelque part dans l'historique. Le fichier `version` devrait toujours avoir le format `v1.x.x` ou `v2.x.x`.

## Exercice 1: Bisect Manuel

```bash
# Démarrer bisect
git bisect start

# Marquer l'état actuel comme cassé
git bisect bad HEAD

# Trouver un ancien commit bon
git log --oneline -10
git bisect good <commit-sha>

# À chaque itération, tester:
cat version

# Si valide (v1.x.x ou v2.x.x):
git bisect good

# Si invalide:
git bisect bad

# Quitter bisect
git bisect reset
```

## Exercice 2: Bisect Automatisé

```bash
git bisect start
git bisect bad HEAD
git bisect good <commit-initial>
git bisect run ./check_version.sh
git bisect reset
```

Le script `check_version.sh` retourne:
- **0** si version valide
- **1** si version invalide
