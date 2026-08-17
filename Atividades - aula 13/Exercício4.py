# Melhore o desafio #09, mostrando a tabuada de um número que o usuário escolher, mas desta vez utilizando o laço for.

n = int(input('Digite um número para saber sua tabuada: '))
for c in range(0,11):
    tab = n * c
    print(f'{n} x {c} = {tab}')
