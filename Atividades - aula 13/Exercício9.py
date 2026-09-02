# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#base
from datetime import date
ano_atual = date.today().year
menoridade = 0
maioridade = 0

for c in range(1,8):
    nascimento = int(input('Qual sua data de nascimento? '))
    if ano_atual - nascimento < 18:
        menoridade += 1

    else:
        maioridade += 1
        
print(f'{menoridade} são de menor e {maioridade} são de maior. ')
