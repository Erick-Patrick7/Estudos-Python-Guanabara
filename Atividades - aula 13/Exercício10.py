# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []  
for pessoa in range(1,6):
    peso = float(input(f'Qual o peso da pessoa {pessoa}? '))
    lista.append(peso)
maior_peso = lista[0]

for peso in lista:
    if peso > maior_peso:
        maior_peso = peso
menor_peso = lista[0]

for peso in lista:
    if peso < menor_peso:
        menor_peso = peso

print(f' O menor peso é: {menor_peso} e o maior é: {maior_peso}')
