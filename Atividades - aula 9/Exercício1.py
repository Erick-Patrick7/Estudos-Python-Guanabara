# Crie um programa que leia o nome completo e mostre: Nome com todas maiúsculas, nome com todas minúsculas, letras totais e quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
u = nome.upper()
l = nome.lower()
total = len(nome) - nome.count(' ')
p = nome.split()[0]
pn = len(p)
print(f'{nome} em maiusculas: {u}')
print(f'Seu nome em minúsculas: {l}')
print(f'Seu nome tem {total} letras no total e no primeiro nome tem {pn}.')
