""" Faça um programa que leia o nome completo de uma pessoa e exiba na tela, o nome da pessoa com letras maiúsculas, o nome completo com as letras minúsculas, quantidade de caracters, sem contar os espaçamentos,e quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: '))
#nome em letra maiúscula 
print('O nome em letras maísculas: ',nome.upper())
#nome com letras minúsculas
print('O nome em letras minúsculas:',nome.lower())
#quantidade de caracters sem contar os espaçamentos
sEspaço = len(nome) - nome.count(" ")
print(f'A quantidade de caracters sem os espaços é de: {sEspaço}')
#Exibir quantas letras tem o primeiro nome
pNome = nome.split()
print('A quantidade de caracters no primeiro nome é de: ', len(pNome[0]))
