#!/bin/bash
# Script de test pour l'exercice git bisect
# Retourne 0 si version valide, 1 sinon

if [ ! -f "version" ]; then
  exit 1
fi

VERSION=$(cat version)

if [[ $VERSION =~ ^v[1-2]\.[0-9]+\.[0-9]+$ ]]; then
  exit 0
else
  exit 1
fi
