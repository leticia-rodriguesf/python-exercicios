print('------------------------------------------------')
lado1 = float(input('Digite um lado do triângulo: '))
lado2 = float(input('Digite outro lado do triângulo: '))
lado3 = float(input('Digite um outro lado do triângulo: '))

if (lado1 < lado2+lado3 and lado2 < lado1 + lado3 and lado3 < lado1+lado2):
    print('------------------------------------------------')
    print('PODEMOS FORMAR UM TRIÂNGULO!')
    if lado1 == lado2 == lado3 == lado1:
        print('E esse triângulo irá ser EQUILÁTERO!')
    elif lado1 != lado2 != lado3 != lado1:
        print('E esse triângulo irá ser ESCALENO!')
    else:
        print('E esse triângulo irá ser ISOSCELES')
else:
    print('NÃO PODEMOS FORMAR UM TRIÂNGULO!')
print('------------------------------------------------')
