import math
print('==='*20)
catetoOposto = float(input('Digite o valor do C.O: '))
catetoAdja = float(input('Digite o valor do C.A: '))
#hipotenusa = math.sqrt(pow(catetoOposto,2) + pow(catetoAdja,2))
hipotenusa = math.hypot(catetoOposto, catetoAdja)
print('O valor do C.O é {} e C.A é {}, já a hipotenusa {:.2f}' .format(catetoOposto,catetoAdja,hipotenusa))
print('==='*20)