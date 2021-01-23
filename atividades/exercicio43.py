print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=')
if (imc < 18.5):
    print('Seu IMC é de {:.2f}'.format(imc))
    print('ABAIXO DO PESO')
elif (imc == 18.5) or (imc < 25):
    print('Seu IMC é de {:.2f}'.format(imc))
    print('PESO IDEAL')
elif (imc == 25) or (imc < 30):
    print('Seu IMC é de {:.2f}'.format(imc))
    print('SOBREPESO')
elif (imc == 30) or (imc < 40):
    print('Seu IMC é de {:.2f}'.format(imc))
    print('OBESIDADE')
else:
    print('Seu IMC é de {:.2f}'.format(imc))
    print('OBESIDADE MÓRBIDA')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=')