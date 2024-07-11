soma = 0
lista = []
for i in range (0, 5):
    num = int(input('Digite um número:'))
    lista.append(num)
print(lista)

for elemento in lista:
    soma += elemento
print(f'A soma dos elementos da lista é: {soma}')

# outro método de somar os valores da lista
#soma = sum(lista)
#print(soma)