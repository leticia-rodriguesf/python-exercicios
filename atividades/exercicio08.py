print('=='*30)
print('             CONVERSOR DE MEDIDAS                  ')
print('=='*30)
m = int(input('Digite o valor em metros: '))
k = m / 1000
hm = m / 100
dam = m /10
dm = m *10
cm = m*100
mm = m*1000
print('O valor em Kilometros: {} km \nO valor em hectômetro: {} hm'.format(k,hm))
print('O valor em dametro: {}dam \nValor em metros: {}m \nValor em decimetro: {}dm'.format(dam,m,dm))
print('O valor em centimetro: {} cm ' .format(cm))
print('Valor em milimetros: {} mm '.format(mm))
print('=='*30)