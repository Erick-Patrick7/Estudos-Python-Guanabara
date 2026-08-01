from random import randint
n = randint(0,5)
n_escolhido = int(input('Qual o número escolhido? '))
if n_escolhido == n:
    print('Parabéns, você acertou!')
else:
    print('Você errou.')
