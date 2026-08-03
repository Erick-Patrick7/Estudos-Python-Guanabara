

# base
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão.
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')
escolha = int(input('Sua escolha: '))

# condições
if escolha == 1:
    print(f'{numero} convertido para BINÁRIO é igual a: {bin(numero)[2:]}')

elif escolha == 2:
    print(f'{numero} convertido para OCTAL é igual a: {oct(numero)[2:]}')

elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a: {hex(numero)[2:]}')

else:
    print('Escolha inválida. Tente novamente. ')

