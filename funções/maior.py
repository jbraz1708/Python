""""Função que descobre o maior número"""

from time import sleep

def maior(* num):
    cont = 0 
    maior = 0
    print('\nAnalisando os valores')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'\nO maior valor informado foi {maior}')

maior(2,5,6,7,1)
maior(4,7,0)