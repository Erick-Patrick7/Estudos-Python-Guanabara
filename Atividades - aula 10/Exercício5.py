# escreva um programa que leia um nao e diga se é bissexto ou não.

a = int(input('Que ano você quer analisar? '))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('é bissexto')
        else:
            print('não é bissexto')
    else:
        print('é bissexto')
else:
    print('não é bissexto')
