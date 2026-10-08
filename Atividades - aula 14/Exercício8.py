# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

c = -1
soma = -999
num = 0
while num != 999: 
    num = int(input('Digite um número [999 para parar]:  '))
    soma += num
    c += 1
print(f'Foram digitados {c} números no total e a soma entre eles é: {soma} ')
