# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário? R$:  '))
aumento = salario * 0.15

if salario > 1250:
    aumento = salario * 0.10

total = aumento + salario
print(f'o aumento é de: {aumento:.2f} e o seu novo salário fica: {total:.2f}')
