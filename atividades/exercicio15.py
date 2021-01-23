dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foi rodado? '))
valor = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f},00'.format(valor))