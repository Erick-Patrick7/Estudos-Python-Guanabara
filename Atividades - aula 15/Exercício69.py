# Exercício 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

from time import sleep

maiores = 0
homens = 0
mulheres = 0

while True:
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Quantos anos você tem: '))
    
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <=19:
        mulheres += 1
    
    continuar = str(input('Quer continuar?  ')).strip().upper()[0]

    if continuar == 'S':
        print('Próximo...')
        sleep(1)
    elif continuar == 'N':
        break
print(f'Tem {maiores} com mais de 18 anos.\nTemos {homens} homens cadastrados e {mulheres} mulheres com menos de 20 anos. ')
