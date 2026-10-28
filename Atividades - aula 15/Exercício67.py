# Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

import time

while True:
    print('-=' * 23)
    num = int(input('Digite um número para revelar sua tabuada: '))
    if num < 0:
        break
    print('-=' * 23)
    print(('Processando...'))
    time.sleep(0.8)
    
    for c in range(1,11):
        resultado = num * c  
        print(f'{num} x {c} = {resultado}')
print('Programa encerrado, digite apenas números positivos.')
