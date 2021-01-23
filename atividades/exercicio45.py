import random
lista = ['pedra','papel','tesoura']
valor = str(input('Pedra, papel ou tesoura? '))
boot = random.choice(lista)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if (valor == boot):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: EMPATE')

elif (valor == 'papel') and (boot == 'tesoura'):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: Computador GANHOU')

elif (valor == 'papel') and (boot == 'pedra'):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: Jogador GANHOU')

elif (valor == 'pedra') and (boot == 'papel'):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: Computador GANHOU')

elif (valor == 'tesoura') and (boot == 'papel'):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: Jogador GANHOU')

elif (valor == 'pedra') and (boot == 'tesoura'):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: Jogador GANNHOU')

elif (valor == 'tesoura') and (boot == 'pedra'):
    print('Jubileu PC jogou {}'.format(boot))
    print('Jogador jogou {}'.format(valor))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('SITUAÇÃO: Computador GANHOU')
else:
    print('ERROR 404! OPÇÃO INVÁLIDA')