# Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM / 14 anos: INFANTIL / 19 anos: JÚNIOR / 25 anos: SÊNIOR / Acima de 25 anos: MASTER

from datetime import date

# base
atual = date.today().year
nascimento = int(input('Em que ano você nasceu: '))
idade = atual - nascimento

# Condições
if idade <= 9:
    print(f'O participante tem {idade} anos, e por isso está na categoria: MIRIM.')

elif idade <= 14:
    print(f'O participante tem {idade} anos, e por isso está na categoria: INFANTIL.')

elif idade <= 19:
    print(f'O participante tem {idade} anos, e por isso está na categoria: JÚNIOR.')

elif idade <= 25:
    print(f'O participante tem {idade} anos, e por isso está na categoria: SÊNIOR.')

else:
    print(f'O participante tem {idade} anos, e por isso está na categoria: MASTER.')
