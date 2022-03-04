nome = str(input('qual o seu nome Professor(a) '))
print('Prazer em te conhecer Professor(a) {:-^20}! \n'.format(nome))

nome = str(input(' Digite o nome do aluno(a): '))
n1 = int(input(' Digite a primeira nota do aluno(a): '))
n2 = int(input(' Digite a segunda nota do aluno(a): '))
media = (n1+n2)/2

print(' A média das notas de {} foi : {}'.format(nome, media))

