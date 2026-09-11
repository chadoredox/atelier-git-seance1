# Journal des incidents (etape 4 et 7)

## 1. Cherry-pick d'un hotfix

Un bug urgent sur `moyenne_ponderee()` a ete corrige sur la branche
`feature/generateur-stats` (commit `930032d`) alors que la branche n'etait
pas prete a etre fusionnee. Le correctif a ete porte sur `main` sans
fusionner le reste du travail :

```
git cherry-pick 930032d -x
```

Resultat : le commit porte sur main a le SHA `cce23dc` (different de
l'original `930032d` — Git cree un NOUVEAU commit) mais un contenu
strictement identique. L'option `-x` ajoute la reference au commit
d'origine dans le message. Le doublon a ensuite disparu de la branche
lors du rebase (patch deja applique).

## 2. git bisect : isolation du commit fautif

Un bug de variance (diviseur `len(valeurs)*2`) a ete introduit par le
commit `db65cf0` ("feat(stats): ajoute un generateur de rapport").
Le script `scripts/test_stats.py` verifie de facon reproductible que
`rapport([1,2,3,4])` contient `variance=1.25`.

```
git bisect start HEAD 6b3747e
git bisect run python scripts/test_stats.py
# -> bisect found first bad commit: db65cf0
git bisect reset
```

Chaque reponse good/bad s'appuie sur le test, jamais sur l'intuition.
Le bug a ensuite ete corrige par `b0e31a7`.

## 3. Hook anti-secret : demonstration (etape 7)

Tentative de commit d'un faux secret :

```
$ git add src/config.py.bak && git commit -m "chore: oops sauvegarde config"
2:STRIPE_API_KEY = "sk_live_5****REDACTED-FICTIF****456"
[pre-commit] SECRET DETECTE dans src/config.py.bak - commit refuse.
[pre-commit] Un secret entre dans l'historique est tres couteux a retirer.
>>> exit code: 1  ->  commit REFUSE
```

Un commit legitime passe sans entrave. Activation du hook :
`git config core.hooksPath githooks`.
