# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

from time import sleep

caros = 0
gasto = 0
menor = 0
c = 0
mnrvalor = ' '

while True:
    
    produto = str(input('Insira nome do produto: ')).strip()
    preço = float(input('Insira o valor do produto R$:'))
    c += 1
    gasto += preço

    if preço >= 1000:
        caros += 1
    if c == 1 or preço < menor: 
        menor = preço
        mnrvalor = produto 
    continuar = str(input('Tem mais produtos? [S/N]: ')).strip().upper()
    
    if continuar == 'S':
        print('===== Próximo produto =====')
        sleep(1)
    elif continuar == 'N':
        break
print(f'O total de gastos na compra é de R$:{gasto:.2f}')
print(f'Você adquiriu {caros} produtos acima de R$:1.000')
print(f'O produto mais barato é o: {mnrvalor}. Custando apenas R$:{menor:.2f}')
