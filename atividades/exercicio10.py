print('=='*20)
print('     QUANTOS DOLÁRES EU TENHO?    ')
money = float(input('Quanto você tem na carteira? R$ '))
dol = money/3.27
print('Hoje o dólar está R$ 3,27 | Você pode comprar U$ {:.2f}! \nEae vai querer? '.format(dol))
print('=='*20)