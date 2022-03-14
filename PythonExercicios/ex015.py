nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:=^20}! \n'.format(nome))

km = float(input('Digite quantos Kilometros foram percorridos pelo carro: '))
dia = int(input('Digite por quantos dias o Carro esteve alugado: '))
precoAluguel = 60 * dia
precoKm = km * 0.15
final = precoKm + precoAluguel

print(f'Você andou {km} Km e Alugou o carro por {dia} dias\n.O valor final a ser pago é de {final} R$ ')
