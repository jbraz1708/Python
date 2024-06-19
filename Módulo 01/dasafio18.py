""" faça um programa que leia o ângulo e exiba o seno o cosseno e a tangente do mesmo. """

import math
ang = int(input('Digite o ângulo para exibir o seno, cosseno e a tangente: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f'O seno do ângulo proposto é: {sen:.2f}, o cosseno é: {cos:.2f}, e a tangente é: {tang:.2f}')
