"""Faça um programa que leia três número e informe entre eles qual o maior e qual o menor número"""

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))
#Verificando quem é menor colocando a como um parâmetro menor
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior colocando a como um parâmetro maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior número é: {maior}')
print(f'O manor número é: {menor}')