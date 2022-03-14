#!/bin/python3

from emoji import * 
from datetime import *
from random import randint

# Mettre les définitions de fonction ci-dessous

def roule_de():
  print(python, 'peut faire un', dice)
  max = input('Combien de côtés ?') # obtient l'entrée de l'utilisateur
  print('C\'est un D', max) # utilise le nombre saisi par l'utilisateur
  roule = randint(1, int(max)) # génère un nombre aléatoire 
  print('Tu as tiré un', roule) # imprime la valeur de la variable roule
  print(fire * roule) # répéter le texte fire plusieurs fois

def hobbies():
  hobby = input('Qu\'est-ce que tu aimes ?')
  print('Ça sonne', fun)
  print('Tu pourrais faire un projet ', python, 'à propos de ', hobby)

# Caractères utiles :',()*_/.#

# Mettre le code à exécuter ci-dessous
print('Bonjour', world)
print('Bienvenue à', python)

input() # attend que l'utilisateur appuie sur Entrée

print(python, 'est très bon en', sums)
print(230 * 5782 ** 2 / 23781)

input()

print('Le', calendar, clock, 'est', datetime.now()) # affiche la date et l'heure actuelles avec emoji 

input()

roule_de() # Appelle la fonction roule_de

input()

hobbies() # Appelle la fonction hobbies




