from math import radians, sin, cos, tan

nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:=^20}! \n'.format(nome))

angulo = int(input('Digite o angulo: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))