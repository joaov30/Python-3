nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

print('insira abaixo as medidas para saber a área\n')

largura = int(input('Digite a Largura\n'))
altura = int(input('Digite a Altura\n'))
area = largura * altura
tinta = area/2

print('A area é igual: {} será necessario {} litros de tinta para pintar a área'.format(area, tinta))