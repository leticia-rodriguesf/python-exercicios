print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print('     VAMOS FORMAR UM TRIÂNGULO?     ')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
lado1 = float(input('Digite o primeiro segmento: '))
lado2 = float(input('Digite o segundo segmento: '))
lado3 = float(input('Digite o terceiro segmento: '))
if lado1 < lado2+lado3 and lado2 < lado1 + lado3 and lado3 < lado1+lado2:
        print('PODEMOS FAZER UM TRIÂNGULO COM ESTES SEGMENTOS!!')
else:
        print('NÃO PODEMOS FAZER UM TRIÂNGULO COM ESTES SEGMENTOS!!')