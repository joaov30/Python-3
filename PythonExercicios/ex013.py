nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

salario = float(input('Digite o seu salário \n'))
aumento = int(input('Digite quantos % de aumento será adicionado '))
novo = salario + (salario * aumento/100)

print('O seu salario originalmente seria de {}.\n Com o aumento passa a ficar {} '.format(salario, novo))
