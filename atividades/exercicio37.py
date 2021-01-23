num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
option = int(input('Sua opção: '))
if  option == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é {}'.format(num,oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('número inválido!')