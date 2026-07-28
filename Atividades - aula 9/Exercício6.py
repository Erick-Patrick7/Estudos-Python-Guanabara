#Faça um programa que leia um nome completo, mostrando em seguida o primeiro e o último nome separadamente.

nome = (input('Digite seu nome completo: ')).strip()
nomes = nome.split()
print(f'Primeiro nome: {nomes[0]}')
print(f'Ultimo nome: {nomes[-1]}')
