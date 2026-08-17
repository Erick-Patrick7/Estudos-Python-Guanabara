#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

resultado = 0
for c in range(3, 501, 6):               
        resultado = resultado + c
         
print(f'a soma entra os números ímpares de 0 a 500 divisíveis por 3 é: {resultado}')
