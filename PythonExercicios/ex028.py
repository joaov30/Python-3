import random
print('Bem vindo ao ogo de advinhação!!')
chute = int(input('Digite um numero entre 0 e 5: '))
numeros = random.randrange(6)


if chute > 5 or chute < 0:
    print('Digite um valor entre 0 e 5!')
    
if numeros == chute:
    print('VOCE ACERTOU PARABENS!!')
    print(numeros)
else:
    print('Voce errou 😔')
    print('O numero certo era {}'.format(numeros))







