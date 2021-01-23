print('-=-'*20)
km = float(input('Digite a velocidade de seu carro: '))
if km > 80:
    multa = (km-80)*7
    print('Você excedeu o limite de velocidade, na qual é de 80km/h!')
    print('Você recebeu uma multa de R${:.2f}, por andar em alta velocidade!'.format(multa))
    print('-=-' * 20)
print('Tenha um bom dia! Dirija com segurança!')
print('-=-'*20)