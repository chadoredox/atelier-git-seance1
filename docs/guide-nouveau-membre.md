# Guide du nouveau membre

Bienvenue dans le groupe ! Pour contribuer a ce depot :

## 1. Installation

```bash
git config --global user.name "Prenom Nom"
git config --global user.email "vous@exemple.com"
git clone https://github.com/chadoredox/atelier-git-seance1.git
cd atelier-git-seance1
```

## 2. Travailler sur une branche

```bash
git switch main && git pull
git switch -c feature/mon-sujet
# ... commits au format conventional commits ...
git push -u origin feature/mon-sujet
```

## 3. Ouvrir une pull request

- Titre : `type(scope): description` (voir le README).
- Description : **quoi** et **pourquoi**.
- Le reviewer est assigne automatiquement selon la zone touchee (voir `CODEOWNERS`).

## 4. Regles a retenir

- Jamais de push direct sur `main` (protection activee).
- Historique lineaire : merge en rebase uniquement.
- Toute PR doit etre revee par le proprietaire de la zone avant merge.
