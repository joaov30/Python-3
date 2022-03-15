nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:=^20}! \n'.format(nome))

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (ad ** 2 + op ** 2) ** (1/2)

print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
