km = int(input('Qual a distância de sua viagem (km/h)? '))
if km <= 200:
    total = km * 0.50
    print('Você terá de pagar R${:.2f}'.format(total))
else:
    total = km*0.45
    print('Você terá de pagar R${:.2f}'.format(total))