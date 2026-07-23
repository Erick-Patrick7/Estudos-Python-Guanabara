preco = float(input('Preço original do produto: '))
desconto = 0.95
promocao = preco * desconto
print(f'o preço original era: {preco} com a promoção fica: {promocao}')

preco = float(input('Qual o preço do produto R$: '))
novo = preco - (preco *5 / 100)
print(f'o produto que custava R$: {preco}, na promoção com 5% de desconto vai custar R$: {novo}')