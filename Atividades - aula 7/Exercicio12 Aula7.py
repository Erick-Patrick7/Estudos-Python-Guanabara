km = float(input('quantos km percorreu? '))
dias = float(input('quantos dias ficou com o carro? '))
pagar_km = km * 0.15
pagar_dia = 60 * dias
print(f'O valor a pagar por km percorridos é R${pagar_km:.2f}')
print(f'O valor a pagar por dias com o veículo é R${pagar_dia:.2f}')
total = pagar_dia + pagar_km
print(f'O valor total a ser pago é R$: {total:.2f}')