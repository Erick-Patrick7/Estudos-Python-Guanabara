'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''


# base
peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura * altura)

# condiçoes
if imc < 18.5:
    print(f'Seu imc é {imc:.2f} Você está abaixo do peso. ')

elif imc < 25:
    print(f'Seu imc é {imc:.2f} Você está no peso ideal. ')

elif imc < 30:
    print(f'Seu imc é {imc:.2f} Você está sobrepeso. ')

elif imc < 40:
    print(f'Seu imc é {imc:.2f} Você está na categoria: OBESIDADE. ')

else:
    print(f'Seu imc é {imc:.2f} você está na categoria OBESIDADE MÓRBIDA. ')
