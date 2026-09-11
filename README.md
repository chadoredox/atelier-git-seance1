# Atelier Git avancé & collaboratif — Séance 1

> Bloc DevOps — dépôt de travail du groupe.

## Membres du groupe

| Rôle | GitHub | Email |
|------|--------|-------|
| Membre 1 (créateur du dépôt) | [@chadoredox](https://github.com/chadoredox) | chadylabib01@gmail.com |
| Membre 2  tan@et.intechinfo.fr |
| Membre 3  ceron@et.intechinfo.fr |
| Membre 4  moussadyk@et.intechinfo.fr |

## Stratégie de branches choisie : trunk-based

**Décision prise en groupe (étape 1) :** nous utilisons une stratégie **trunk-based** :
une branche principale unique `main` toujours déployable, sur laquelle tout arrive
via des **pull requests**, et des branches de travail **courtes et éphémères** créées
à partir de `main` et rebasées dessus avant merge.

Ce choix a été préféré à Git Flow (branches `develop`/`release` persistantes) car le
groupe est petit, les itérations sont courtes, et il simplifie l'application de
l'**historique linéaire** imposé par la protection de branche .

### Convention de nommage des branches



| `feature/<sujet>` | nouvelle fonctionnalité | `feature/calcul-moyenne` |
| `fix/<sujet>` | correction de bug non urgent | `fix/division-zero` |
| `hotfix/<sujet>` | correctif urgent à porter rapidement | `hotfix/fuite-memoire` |
| `chore/<sujet>` | maintenance, tooling, docs | `chore/ci-setup` |

- Toujours en `kebab-case`, à partir de `main` à jour.
- Durée de vie courte : mergée ou supprimée dès que la PR est fermée.

### Règle de merge

- **Une PR obligatoire pour tout changement sur `main`** (protection de branche).
- Merge en **rebase** (`Rebase and merge`) : l'historique de `main` reste linéaire.
- Commits conformes aux **Conventional Commits** (`type(scope): description`).


## Structure du dépôt

```
.
├── README.md            # ce fichier : décisions et documentation de l'atelier
├── .gitignore           # exclusions (secrets, IDE, OS, artefacts de build)
├── CODEOWNERS           # propriétaires par zone du dépôt (étape 5)
├── src/                 # code de l'application
├── docs/                # documentation du groupe
└── scripts/             # scripts utilitaires (tests, bisect, etc.)
```


