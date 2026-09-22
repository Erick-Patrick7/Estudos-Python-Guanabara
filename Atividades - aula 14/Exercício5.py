# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-=' * 10)
print('10 Termos de uma PA')
print('-=' * 10)

pt = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
termo = pt
c = 1

while c <= 10:
    print(termo, end=' ')
    termo += razao
    c += 1
      