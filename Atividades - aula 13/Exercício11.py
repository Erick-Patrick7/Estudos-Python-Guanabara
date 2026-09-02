# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo, 
# Qual é o nome do homem mais velho 
# Quantas mulheres têm menos de 20 anos.

total_idade = 0
idade_velho = 0
nome_velho = ''
menosde20 = 0

for pessoa in range(1,5):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    genero = input('Gênero (F/M): ').strip()

    total_idade += idade

    if genero in 'Mm':
        if nome_velho == '' or idade > idade_velho:
            idade_velho = idade
            nome_velho = nome

    if genero in 'Ff' and idade < 20:
        menosde20 += 1

media_idade = total_idade / 4

print(f'{menosde20} delas são mulheres com menos de 20 anos. ')
print(f'A média de idade do grupo é: {media_idade}')
print(f'O homem mais velho se chama: {nome_velho} e tem: {idade_velho} anos')
