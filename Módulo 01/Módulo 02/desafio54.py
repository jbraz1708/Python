maior = 0 # contadores
menor = 0 # contadores
from datetime import date
atual = date.today().year # ano atual
for i in range (1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = atual - nasc 
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Quantidade de Pessoas maiores de idade na lista: {maior}')
print(f'Quantidade de pessoas menores de idade na lista: {menor}')