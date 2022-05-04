velocidade = float(input('Digite a velocidade do seu carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você esta acima do limite permitido de 80km, você sera multado em R$7.00 reais por cada km acima do limite')
    print('O valor de sua multa é de {}'.format(multa))
else:
    print('Esta dentro do limites dirija com segurança')