#Variáveis iniciais 
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
#Programa
print("""  ======= Selecione uma operação ======= 
[1] divisão
[2] multiplicação
[3] soma
[4] subtração""")
#Option
option = float(input('Escolha sua Operação --- '))
#Condição
if option == 1:
    divi = n1 / n2 
    print(f'A divisão entre {n1}, e {n2} é igual há: {divi} ')
elif option == 2:
    mult = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é igual há: {mult}')
elif option == 3:
    soma = n1 + n2
    print(f'A soma entre {n1} e o {n2} é igual há: {soma}')
elif option == 4:
    sub = n1 - n2
    print(f'A subtração entre {n1} e o {n2} é igual há: {sub} ')
else:
    print('Digite uma opção coerente!')