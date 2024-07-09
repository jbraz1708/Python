termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for i in range (termo, decimo, razao):
    print(i, end=' > ')
print('Acabou!')
   
