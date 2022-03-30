#!/bin/python3

from emoji import * 
from datetime import *
from random import randint

# Pon las definiciones de función aquí abajo

def lanzar_dado():
  print(python, 'puede crear un', dice)
  max = input('¿Cuántas caras?') # Obtener entrada del usuario
  print('Es un D', max) # Usa el número que el usuario introdujo
  lanzar = randint(1, int(max)) # Genera un número aleatorio 
  print('Lanzaste un', lanzar) # Imprime el valor de la variable del tiro
  print(fire * lanzar) # Repite el texto de fuego las veces del resultado del tiro

def pasatiempos():
  pasatiempo = input('¿Qué te gusta?')
  print('Eso suena', fun)
  print('Podrías hacer un proyecto', python, 'sobre', pasatiempo)

# Caracteres útiles :',()*_/.#

# Pon el código a ejecutar aquí abajo
print('Hola', world)
print('Bienvenido a', python)

input() # Espera a que el usuario presione Enter

print(python, 'es muy bueno en', sums)
print(230 * 5782 ** 2 / 23781)

input()

print('La', calendar, clock, 'es', datetime.now()) # Imprime la fecha y hora actual con emoji 

input()

lanzar_dado() # Llama a la función lanzar_dado

input()

pasatiempos() # Llama a la función pasatiempos




