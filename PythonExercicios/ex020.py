import random

print('Bem Vindo\n')

p1 = str(input('Digite o nome do primeiro aluno \n'))
p2 = str(input('Digite o nome do segundo aluno \n'))
p3 = str(input('Digite o nome do terceiro aluno \n'))
p4 = str(input('Digite o nome do quarto aluno \n'))
grupo = [p1, p2, p3, p4]
random.shuffle(grupo)

print(grupo)