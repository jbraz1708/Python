alunos = {}

for i in range (3):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    alunos[nome] = nota 
print(alunos)

media = sum(alunos.values()) / (len(alunos))
print(media) 