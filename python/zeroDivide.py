def spam(divideBy):
    return 42 / divideBy

try:
   print (spam(2))
   print (spam(12))
   print (spam(0))
   print (spam(1))
except ZeroDivisionError:
   print('Hubo una division por cero, se debe revisar')
