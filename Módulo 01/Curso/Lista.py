qnt = int(input('Digite a quantidade de carros que você deseja cadastrar: '))
l1 = []
l2 = []

for i in range (0, qnt):
    nome_carro = input('Digite o nome de um carro: ')
    l1.append(nome_carro)
    ano_carro = int(input('Digite o ano do veículo: '))
    l2.append(ano_carro)
for i in range (0, qnt):
    print(f'O Modelo {l1[i]} é do ano {l2[i]} ')
