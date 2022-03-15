from math import hypot

nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:=^20}! \n'.format(nome))

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(op, ad)

print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))