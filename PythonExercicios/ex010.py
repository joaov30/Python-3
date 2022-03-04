nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

reais = int(input('Digite o valor em R$ para converter em U$: '))
dolar = int(5.03)
conversao = dolar * reais

print('Você digitou {} R$, a cotação atual é {}U$. O resultado final é {}U$ '.format(reais, dolar, conversao))