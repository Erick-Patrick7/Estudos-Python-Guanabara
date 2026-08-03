# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


# base
from datetime import date

nascimento = int(input('Em que ano você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

# contrução de condições

if idade > 18:
    passou = idade - 18
    if passou == 1:
        unidade = 'ano'
    else: 
        unidade = 'anos'
    print(f'você ja devia estar alistado a {passou} {unidade}')    

elif idade < 18:
    tempo_restante = 18 - idade
    if tempo_restante == 1:
        unidade = 'ano'
    else:
        unidade = 'anos'
    print(f'Voce deverá se alistar em {tempo_restante} {unidade}')

else:
    print('Essa é a hora certa de se alistar')
