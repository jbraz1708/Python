""""Faça um programa que leia o cateto oposto e o cateto adjacente e exiba o cálculo da hipotenusa"""

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)

print(f'{hi}')
