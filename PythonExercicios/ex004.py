info = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é ', type(info))
print(f'Você digitou {info} possui apenas letras ? = ', info.isalpha())
print('So tem espacos', info.isspace())
print(f'Você digitou {info} possui apenas numeros ? = ', info.isnumeric())
print(f'Você digitou {info}, Possui letras e numeros? ', info.isalnum())
