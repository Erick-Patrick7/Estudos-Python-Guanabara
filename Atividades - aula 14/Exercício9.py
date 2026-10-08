# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


c = soma = menor = maior = 0
res = 'S'

while res in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    c += 1

    if c == 1:
        maior = menor = n

    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    res = input('Quer continuar? [S/N]: ').strip().upper()
    if res == 'N':
        print('Encerrando...\n')

media = soma / c

print(f'Você digitou {c} números. O maior número é: {maior} e o menor é: {menor}')
print(f'A soma é: {soma} e a média é {media:.2f}')
