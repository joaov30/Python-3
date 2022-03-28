nome = str(input('Digite o seu nome: ')).strip()
print('=================')

print('O seu nome em letras é: ', nome.title())
print('O seu nome em letras maiúsculas é: ', nome.upper())
print('O seu nome em letras minusculas é: ', nome.lower())
print(f'O seu nome ao todo possui {len(nome)} letras')
primeiroNome = nome.title().split()
print('O seu primeiro nome é {} e ele tem {} letras '.format(primeiroNome[0], len(primeiroNome[0])))