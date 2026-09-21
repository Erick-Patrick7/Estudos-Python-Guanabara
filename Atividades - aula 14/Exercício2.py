# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tentativas = 1
computador = randint(0,10)
numero = int(input('Escolha um número entre 0 e 10: '))

print('-='*18)
while numero != computador:
    tentativas += 1
    numero = int(input('Número errado. Tente novamente: '))
    print('-='*18)

print('Parabéns você acertou! ')
print(f'O computador escolheu: {computador} e você escolheu {numero}.')
print(f'Você tentou {tentativas} vezes.')
