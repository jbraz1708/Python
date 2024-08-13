"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
 """

def área(larg, comp):
   a = larg * comp
   print(f'A área Calculada é: {a}')

l = int(input('Digite a largura: '))
c = int(input('Digite o comprimento: '))

área(l, c)
