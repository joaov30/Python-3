nome = str(input('qual o seu nome '))
print('Prazer em te conhecer {:-^20}! \n'.format(nome))

n1 = int(input('Digite um número para saber o seu Sucessor e Antecessor'))
antes = n1 - 1
depois = n1 + 1

print('Voce digitou {}, Logo o seu antecessor é {} ja o seu sucessor é {} '.format(n1, antes, depois))
