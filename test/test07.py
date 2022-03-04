nome = str(input('qual o seu nome '))

print('Prazer em te conhecer {:-^20}! \n'.format(nome))
print('O que você gostaria de fazer \n')

escolha = int(input(' Potencia = 1 \n Multiplicação = 2 \n divisão = 3 \n Soma = 4 \n subtração = 5 \n'))


if escolha == 1:
    n1 = int(input('Um valor: '))
    n2 = int(input('Um segundo valor '))
    print('A Potencia vale {}'.format(n1**n2))

if escolha == 2:
    n1 = int(input('Um valor: '))
    n2 = int(input('Um segundo valor '))
    print('A Multiplicação vale {}'.format(n1*n2))

if escolha == 3:
    n1 = int(input('Um valor: '))
    n2 = int(input('Um segundo valor '))
    print('A Divisão vale {}'.format(n1/n2))

if escolha == 4:
    n1 = int(input('Um valor: '))
    n2 = int(input('Um segundo valor '))
    print('A Soma vale {}'.format(n1+n2))

if escolha == 5:
    n1 = int(input('Um valor: '))
    n2 = int(input('Um segundo valor '))
    print('A Subtração vale {}'.format(n1-n2))