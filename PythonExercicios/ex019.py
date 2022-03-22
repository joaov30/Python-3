import random

print('Bem Vindo\n')

a1 = str(input('Digite o nome do primeiro aluno \n'))
a2 = str(input('Digite o nome do segundo aluno \n'))
a3 = str(input('Digite o nome do terceiro aluno \n'))
a4 = str(input('Digite o nome do quarto aluno \n'))
alunos = [a1, a2, a3, a4]
sorteado = random.choice(alunos)

print(sorteado)
