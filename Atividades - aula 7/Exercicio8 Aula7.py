largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
dimensão = altura + largura
area = largura * altura 
print(f'sua dimensão é {dimensão}')
print(f'a parede tem: \nlargura: {largura}\naltura: {altura}')
print(f'sua área é {area:.2f}m²')
tinta = area /2
print(f'é necessário {tinta:.2f} litros de tinta para pinta-la por completo.')