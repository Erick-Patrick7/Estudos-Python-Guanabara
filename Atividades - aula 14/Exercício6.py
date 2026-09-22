# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

total = 0
termo = p_termo
c = 1
mais = 10

while mais != 0:
    total += mais

    while c <= total:
        print(termo,end=' ')
        c += 1
        termo += razao

    mais = int(input('\nQuantos termos a mais você quer mostrar?'))

print(f'O total de termos mostrados foi: {total}')
