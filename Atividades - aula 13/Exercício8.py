# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo

# base
frase = (input('Digite uma frase: ')).strip().lower()
junta = ''.join(frase.split())
invertida = junta[::-1]

#condições
if junta == invertida:
    print(f'A frase: {junta} invertida fica: {invertida}. A frase é um palindromo.')
else:
    print('Não é um palindromo')
