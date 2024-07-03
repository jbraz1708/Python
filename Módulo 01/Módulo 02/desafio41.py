""""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento:'))
idade = atual - nasc
print(f'Sua idade é de {idade} anos')
if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Júnior')
elif idade <= 25:
    print('Categoria Sênior')
else:
    print("Categoria Master")