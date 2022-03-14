nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

n = int(input(' Bem vindo a Tabuada, digite um numero para ver o resultado: '))
multiplicando = 0
cont = 0

while cont <= 10:
    print(n * multiplicando)
    multiplicando = multiplicando + 1
    cont = cont + 1

