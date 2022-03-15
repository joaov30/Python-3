from math import floor

nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:=^20}! \n'.format(nome))

num = float(input('Digite um numero real '))
inteiro = floor(num)

print(f'O número digitado foi: {num} tem a parte inteira igual a {inteiro} ')