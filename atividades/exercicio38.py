num1 = int(input('Digite um valor qualquer: '))
num2 = int(input('Digite qualquer outro valor: '))
print('---'*20)
if (num1 > num2):
    print('O PRIMEIRO valor é maior')
elif (num2 > num1):
    print('O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')