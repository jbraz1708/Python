"""Desenvolva um programa que pergunte a distância de uma viagem em km.Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km, e R$0,45 para viagens maiores que 200km"""

dist = int(input('Quantos KM você vai viajar?'))
if dist <= 200:
    passagem = dist * 0.5
    print(f'O valor da viagem fica de R$ {passagem}')
else:
    passagem = dist * 0.45
    print(f'O valor da viagem fica de R$ {passagem}')
    