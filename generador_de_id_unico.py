import random
from random import randint

nombre = input('Escribe tu nombre: ')
apellido = input('Escribe tu apellido: ')
nacimiento = int(input('Escribe tu fecha de nacimiento: '))
aleatoreo_1 = randint(1,9)
aleatoreo_2 = randint(1,9)
aleatoreo_3 = randint(1,9)
aleatoreo_4 = randint(1,9)


print()  


print(f'Hola {nombre} !')
nombre = nombre[:2].upper()  # Primeros 2 digitos y en mayuscula
apellido = apellido[:2].upper()  # Primeros 2 digitos y en mayuscula
nacimiento = str(nacimiento)[2:]  # Ultimos 2 digitos

print(' Tu numero de identificacion ID generado por el sistema es: ')
print(f'{nombre}{apellido}{nacimiento}{aleatoreo_1}{aleatoreo_2}{aleatoreo_3}{aleatoreo_4}')
