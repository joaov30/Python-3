import random
from time import sleep

print('-----' * 20)
print('Bem vindo ao jogo de advinhação!!')
print('-----' * 20)
print('Estou aguardando sua resposta...\n')
chute = int(input('Digite um numero entre 0 e 5: '))
print('PROCESSANDO....')
numeros = random.randrange(6)

sleep(3)

if chute > 5 or chute < 0:
    print('Digite um valor entre 0 e 5!')

if numeros == chute:
    print('VOCE ACERTOU PARABENS!!')
    print(numeros)
else:
    print('Voce errou 😔')
    print('O numero certo era {}'.format(numeros))







