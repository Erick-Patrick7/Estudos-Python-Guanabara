# Crie um programa que faça o computador jogar Jokenpô com você.

#base
from random import randint
jogador = int(input('''Qual você escolhe:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA 
'''))
computador = randint(0,2)

#condições
if jogador == 0: 
    if computador == 0:
        print('O computador escolheu PEDRA. Deu EMPATE!')
    elif computador == 1:
        print('O computador escolheu PAPEL. Você PERDEU!')
    elif computador == 2:
        print('O computador escolheu TESOURA. Você VENCEU!')

elif jogador == 1:
    if computador == 0:
        print('O computador escolheu PEDRA. Você VENCEU!')
    elif computador == 1:
        print('O computador escolheu PAPEL. Deu EMPATE!')
    elif computador == 2:
        print('O computador escolheu TESOURA. Você PERDEU!')

elif jogador == 2:
    if computador == 0:
        print('O computador escolheu PEDRA. Você PERDEU!')
    elif computador == 1:
        print('O computador escolheu PAPEL. Você VENCEU!')
    elif computador == 2:
        print('O computador escolheu TESOURA. Deu EMPATE!')

else:
    print('JOGADA INVÁLIDA! Tente novamente.')
