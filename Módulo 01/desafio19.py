""""Faça um programa que leia o nome de 4 pessoas e escolha um deles"""
import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))

lista = [n1, n2, n3, n4]
aleatorio = random.choice(lista)

print(f'O aluno escolhido foi: {aleatorio}')


