print('=='*20)
nome = input('Olá, qual é seu nome? ')
x = float(input('Quanto você tirou na parcial? '))
y = float(input('Quanto você tirou na bimestral? '))
media = (x+y)/2
print('- Olá, {}. Acabamos de calcular sua média! e sua média é {:.2f}'.format(nome, media))
print('=='*20)