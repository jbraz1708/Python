tot = 0
num = int(input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}', end=' ')
        tot+= 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f', O número {num} foi divisível {tot} vezes')
if tot == 2:
    print('Número primo')
else: 
    print('Não é um número primo')     
   