"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados"""

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade do número digitado é: {u}')
print(f'A dezena do número digitado é: {d}')
print(f'A centena do número digitado é: {c}')
print(f'A milhar do número digitado é: {m}')