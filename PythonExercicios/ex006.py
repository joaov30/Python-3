nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

n1 = int(input('Digite um numero para saber qual é o seu Dobro,Triplo e sua Raiz Quadrada: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = int(n1 ** (1 / 2))

print('Você Digitou {}, 8 o seu dobro é {} e seu triplo {}\n.A raiz quadrada do número digitado é {}'.format(n1, dobro, triplo, raiz))
