#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", em que posição aparece pela primeira vez e em que posição aprece pela última vez.

frase= input('Digite uma frase: ').strip().lower()
print(f'A letra A aparece {frase.count('a')} vezes na frase')
print(f'A primeira letra A aparece na posição: {frase.find('a') + 1} ')
print(f'A ultima letra A aparece na posicão: {frase.rfind('a') + 1}')
