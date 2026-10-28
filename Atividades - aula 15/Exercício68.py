# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
import random

c = 0
while True:
    computador = random.randint(1,10) # computador escolhe um número
    print('-=' * 10)
    player = int(input('Escolha um número: ')) # player escolhe um número
    print('-=' * 10)
    escolha = str(input('\nVocê quer par ou Ímpar: ')).strip().upper()[0]
    num = computador + player
    if escolha not in ('P', 'Í', 'I'):
        print('inválido. Por favor escolha apenas entre Par ou Ímpar.\n')
        sleep(1)
        print('Vamos de novo...')
    else: 
        print(f'\nO computador escolheu: [{computador}] o player escolheu: [{player}] o número é: [{num}]')
        if escolha == 'P':
            if num % 2 == 0:
                print('Você ganhou!')
                c += 1
            else:
                print('O número é Ímpar... Você perdeu.')
                break
        elif escolha in ('Í', 'I'):
            if num % 2 == 1:
                print('Você venceu!')
                c += 1
            else:
                print('O número é Par... Você perdeu.')
                break 
if c >= 10:
    print(f'\nUau! você é um ótimo player... Você venceu {c} vezes.')
elif c >= 5:
    print(f'\nParabéns! você venceu {c} vezes')
elif c >= 3:
    print(f'\nVocê venceu {c} vezes.')
elif c == 0:
    print(f'\nhaha! lhe falta sorte...')
