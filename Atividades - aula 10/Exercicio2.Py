# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 60km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('velocidade do carro: '))
if velocidade <=60:
    print('Você esta dentro do limite de (60km), Pode seguir.')
else:
    excesso = velocidade - 60
    multa = excesso * 7
    print(f'Você foi MULTADO! Motivo: exceder o limite de velocidade (60km)')
    print(f'O valor da multa é de R$: {multa:.2f}')
