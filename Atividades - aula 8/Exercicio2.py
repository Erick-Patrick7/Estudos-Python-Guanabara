import math
co = float(input('Qual é o tamanho do cateto oposto? '))
ca = float(input('Qual é o tamanho do cateto adjacente? '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir: {hi:.2f}')