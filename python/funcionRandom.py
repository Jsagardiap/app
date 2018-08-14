import random
def respuesta(numero):
    if numero == 1:
       return 'Numero Uno'
    elif numero == 2:
       return 'Numero Dos'
    elif numero == 3:
       return 'Numero Tres'
    elif numero == 4:
       return 'Numero Cuatro'

numeroRandom = random.randint(1, 4)
numeroFinal =  respuesta(numeroRandom)
print (numeroFinal)

