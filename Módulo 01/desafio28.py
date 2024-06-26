""""Escreva um programa que faça o computador pensar em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, o programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random
user = int(input('Adivinhe o número em que o computador está pensando: '))
pc = random.randint(1, 5)
if pc == user:
    print("Venceu!")
else:
    print("Perdeu, tente novamente!")
print(f'Número em que o pc pensou : {pc}')