# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-='*10)
print('10 termos de uma PA')
print('-='*10)

pt = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))

termo = pt + (10 - 1) * razao

for c in range(pt, termo + razao, razao):
    print(c)
print('FIM')
