# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opçoes = 0

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

while opçoes != 5:
    opçoes = int(input('''Escolha uma das opções abaixo: 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do  programa '''))

    if opçoes == 1:
        soma = v1 + v2
        print(f'A soma entre {v1} e {v2} é: {soma}')

    elif opçoes == 2:
        mult = v1 * v2
        print(f'A multiplicação entre {v1} e {v2} é: {mult}')

    elif opçoes == 3:
        if v1 > v2:
            print(f'O primeiro valor ({v1}) é maior. ')

        elif v2 > v1:
            print(f'O segundo valor ({v2}) é maior. ')

        elif v1 == v2:
            print('Os valores são iguais. ')

    elif opçoes == 4:
        v1 = int(input('Digite um novo valor: '))
        v2 = int(input('Digite outro valor: '))

    elif opçoes == 5:
        print('Programa finalizado. ')
