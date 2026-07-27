#Crie um programa que leia o nome de uma cidade e diga se começa ou não com o nome "SANTO".

cdd = input('Qual é a sua cidade natal? ').strip().upper()
print(cdd[:5] == 'SANTO')
