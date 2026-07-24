from math import sin, radians, cos, tan
ang = float(input('Digite o ângulo: '))
s = sin(radians(ang))
print(f'O ângulo de: {ang} tem o SENO: {s:.2f} ')
c = cos(radians(ang))
print(f'O ângulo de: {ang} tem o COSSENO: {c:.2f}')
t = tan(radians(ang))
print(f'O ângulo de: {ang} tem a TANGENTE de: {t:.2f}')