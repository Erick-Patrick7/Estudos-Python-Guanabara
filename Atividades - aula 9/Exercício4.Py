#Crie um programa que leia o nome e diga se ela tem "SILVA" no nome.

nome = input('Qual seu nome completo? ').strip().lower()
print(f'Seu nome tem Silva? {"silva" in nome}')
