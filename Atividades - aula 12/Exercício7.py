# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

l1 = float(input('Qual tamanho do primeiro lado: '))
l2 = float(input('Qual o tamanho do segundo lado: '))
l3 = float(input('Qual o tamanho do terceiro lado:  '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os lados podem formar um triângulo.')
   
    if l1 == l2 == l3:
        print('Formato: EQUILÁTERO') 

    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Formato: ISÓSCELES') 
       
    else:
        print('Formato: ESCALENO')
       
else:
    print('Os lados não podem formar um triângulo. ')
