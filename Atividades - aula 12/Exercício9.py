'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

1 - À vista dinheiro/PIX: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço formal 
4 - 3x ou mais no cartão: 20% de juros
'''

# base
preço = float(input('Qual é o valor do produto? '))
print('As Formas de pagameno disponiéis são: \n1. á vista. \n2. á vista no cartão. \n3. em até 2x no cartão. \n4. 3x ou mais no cartão.')
forma = int(input('Qual a foma de pagamento? '))

# descontos
a_vista = preço * 0.10
card = preço * 0.05
juros = preço * 0.20

#condições
if forma == 1:
    total = preço - (preço * 0.10)
    print(f'O preço é R${preço:.2f} pagando á vista você ganha um deconto de R$:{a_vista:.2f}. Você terá de pagar APENAS {total:.2f}')

elif forma == 2:
    total = preço - (preço * 0.05)
    print(f'O preço normal é R${preço:.2f} pagando á vista no cartão você gannha um desconto de R$:{card:.2f}. Você terá de pagar APENAS {total:.2f}')

elif forma == 3:
    total = preço
    parcelado = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcelado:.2f} SEM JUROS.')
    print(f'Pagando em 2x no cartão fica R${total:.2f}')

elif forma == 4:
    total = preço + (preço * 0.20)
    totaldeparcelas =  int(input('Quantas parcelas: '))
    parcela = total / totaldeparcelas
    print(f'O preço é R${preço:.2f}. Sua compra será parcelado em R${parcela}.')
    print(f'Parcelando em {totaldeparcelas}x Você terá de pagar 20% de juros, ficando R${juros:.2f} a mais. O total será de R${total:.2f}. ')

else:
    print(f'Opção inválida.')
