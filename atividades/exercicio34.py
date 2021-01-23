sal = float(input('Digite o salário do funcionário: '))
if sal >= 1250:
    aumento = sal +(sal*(10/100))
    print('Quem tinha o salário de R${:.2f}, agora tem o salário de R${:.2f}!'.format(sal,aumento))
else:
    aumento = sal +(sal*(15/100))
    print('Quem tinha o salário de R${:.2f}, agora tem o salário de R${:.2f}'.format(sal,aumento))
