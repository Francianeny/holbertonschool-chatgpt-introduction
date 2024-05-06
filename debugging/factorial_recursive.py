#!/usr/bin/python3
import sys

# Définition de la fonction pour calculer la factorielle
def factorial(n):
    # Cas de base : si n est 0, retourne 1
    if n == 0:
        return 1
    else:
        # Sinon, récursivement calcule la factorielle de n-1 et multiplie par n
        return n * factorial(n-1)

# Vérifie si le nombre d'arguments passés est différent de 2
if len(sys.argv) != 2:
    # Affiche un message d'erreur si le nombre d'arguments est incorrect
    print("Veuillez fournir un seul argument (le nombre dont vous voulez calculer la factorielle)")
else:
    # Sinon, appelle la fonction factorial avec l'argument passé et affiche le résultat
    f = factorial(int(sys.argv[1]))
    print(f)
