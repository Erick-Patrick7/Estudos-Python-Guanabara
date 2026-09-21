# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

genero = input('Qual seu gênero [F/M]: ').strip().upper()
while genero != 'M' and genero != 'F':
    genero = input('INVÁLIDO. Por favor digite um gênero válido: ').strip().upper()
    
if genero == 'F':
    print('É feminino.')

elif genero == 'M':
    print('É masculino.')
