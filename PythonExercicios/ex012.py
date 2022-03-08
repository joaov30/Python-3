nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

valor = float(input('Digite o preço do item \n'))
desconto = int(input('Digite o valor do Desconto \n'))
novo = valor - (valor * desconto/100)


print('O Preço Original é de {}.\n Com desconto o valor final é {}'.format(valor, novo))