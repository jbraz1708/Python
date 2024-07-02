"""Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão, 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número:'))
print ('''Escolha uma das opções abaixo: 
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal
''')
opção = int(input('Digite sua opção: '))

if opção == 1:
    print(f'O número {num}, em binário fica: {bin(num)[2:]}')
elif opção == 2:
    print(f'O número {num}, em octal fica: {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num}, em hexadecimal fica: {hex(num)[2:]}')
else :
    print('Opção inválida, tente um número entre 1 e 3')


    
