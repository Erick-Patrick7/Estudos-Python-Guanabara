# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:  
# abaixo de 5.0: REPROVADO  
# entre 5.0 e 6.9: RECUPERAÇÃO  
# 7.0 ou superior: APROVADO

nota1 = float(input('Sua primeira nota: '))
nota2 = float(input('Sua segunda nota:  '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'sua média é: {media} você foi REPROVADO.')

elif  5.0 <= media < 7.0:
    print(f'sua média é: {media} você está de RECUPERAÇÃO.')

else:
    print(f'sua média é: {media} Parabéns! Você foi APROVADO.')
