sexo = ''
while sexo != 'M' and sexo!= 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Essa pessoa foi registrada como sexo masculino')
    elif sexo == 'F':
        print('Essa pessoa foi registrada como sexo feminino')
    else: 
        print('Digite uma sigla correta para registar no banco de dados') 
print('---------FIM---------')
