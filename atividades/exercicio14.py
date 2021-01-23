print('=='*20)
c = float(input('Informe a temperatura em °C: '))
f = ( (9 * c) / 5) + 32 #Você pode tirar o parenteses se quiser, pois a ordem de precedencia é igual
k = c + 273
print('Valor em Celsius: {}°C'.format(c))
print('Valor em fahrenheit: {}°F'.format(f))
print('Valor em Kelvin: {}K'.format(k))
print('=='*20)