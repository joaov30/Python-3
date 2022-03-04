nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

metros = int(input('Digite quantos Metros você deseja converter para centimetros: '))
cm = metros * 100
milimetros = metros * 1000

print('{} Metros é igual a {} Centimetros e {} Milimetros '.format(metros, cm, milimetros))