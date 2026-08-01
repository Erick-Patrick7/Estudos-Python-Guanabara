# Desenvolva um programa que leia o comprimento de três rectas 
# e diga ao utilizador se elas podem ou não formar um triângulo.

l1 = float(input('Qual o tamanho do primeiro lado? '))
l2 = float(input('Qual o temanho do segundo lado? '))
l3 = float(input('Qual o tamanho do terceiro lado? '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Sim os lados podem formar um triangulo.')
else:
    print('Não, os lados não podem formar um triangulo.')