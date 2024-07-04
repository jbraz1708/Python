#Variáveis 
salário = float(input('Digite seu salário - R$: '))
#Condição
if salário <= 280:
    aumento = salário * (20 / 100)
    print(f'O aumento foi de 20%: R$ {aumento}')
    nSalário = salário + aumento
    print(f'Seu novo salário é de: R$ {nSalário}')
elif salário > 280 and salário <= 699:
    aumento = salário * (15 / 100)
    print(f'O aumento foi de 15%: R$ {aumento}')
    nSalário = salário + aumento
    print(f'Seu novo salário é de: R$ {nSalário}')
elif salário > 700 and salário <= 1499:
    aumento = salário * (10 / 100)
    print(f'O aumento foi de 10%: R$ {aumento}')
    nSalário = salário + aumento
    print(f'Seu novo salário é de: R$ {nSalário}')
else:
    aumento = salário * (5 / 100)
    print(f'O aumento foi de 5%: R$ {aumento}')
    nSalário = salário + aumento
    print(f'Seu novo salário é de: R$ {nSalário}')
