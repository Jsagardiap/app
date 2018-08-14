# Este aplicativo permite adivinar un numero.

import random

numeroSecreto = random.randint(1, 20)
print ('Estoy pensando en un numero entre 1 y 20')

# Pregutar cuantas veces quiere adivinar

for numero in range(1, 7):
    print('Ingrese un numero:')
    numeroIngresado = int(input())

    if numeroIngresado < numeroSecreto:
       print('El numero ingresado es muy bajo')
    elif numeroIngresado > numeroSecreto:
       print('El numero ingresado es muy alto')
    else:
       break # Numero es correcto

if numeroIngresado == numeroSecreto:
   print('Buen trabajo !! usted adivino el numero en ' + str(numero) + 'intentos')
else:
   print('No fue posible adivinar y el numero que pense fue ' + str(numeroSecreto))

