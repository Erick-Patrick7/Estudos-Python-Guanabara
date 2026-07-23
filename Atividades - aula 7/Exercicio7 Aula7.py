dinheiro = float(input('sua carteira R$: '))
moeda = dinheiro * 100
dollar = dinheiro / 5.47
print(f'você tem R$:{dinheiro:.2f} reais convertendo em moeda fica: {moeda:.2f}')
print(f'com esse valor em reais, você pode comprar um total de $:{dollar :.2f} dolares')