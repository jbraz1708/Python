""" Faça um programa que leia um número e mostre a porção inteira do mesmo!! """

from math import trunc
num = float(input('Digite um número:'))
inteiro = trunc(num)

print(f'A porção inteira do número {num} é: {inteiro}')