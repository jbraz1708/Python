"""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
# importei a biblioteca para verificar o ano
from datetime import date 
atual = date.today().year 
nasc = int(input('Digite seu ano de nascimento:'))
idade = atual - nasc #idade do usuário
print(f'quem nasceu em {nasc} tem {idade} anos em {atual}.')
#Condição
if idade == 18:
    print('Você tem que se alistar imediatamete!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em: {ano} ')
else:
    saldo = idade - 18 
    print(f'Você já deveria ter se alistador há {saldo} anos')
    ano = atual - saldo 
    print(f'Seu alistamento foi em: {ano}')