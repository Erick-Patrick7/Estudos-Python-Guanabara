# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# base
salario = float(input('Qual é o seu salário? R$:'))
casa = float(input('Qual é o valor da casa? R$:'))
tempo = int(input('Pagará em quantos anos? '))

# somas
mensalidade = casa / (tempo * 12)
porcentagem = salario * 0.30
 
# condições do empréstimo
if mensalidade > porcentagem:
    print('Empréstimo NEGADO. Seu salário está abaixo da porcentagem necessária.')

else:
    print('Empréstimo APROVADO. você cumpriu com os requisitos e seu empréstimo foi aprovado! ')
    
print(f' Para pagar uma casa de R$: {casa:.2f} em {tempo} anos, a mensalidade será de R$:{mensalidade:.2f} ')
