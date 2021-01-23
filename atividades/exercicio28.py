from random import randint
from time import sleep
think = randint(0,5)
print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-====-==-==-==-==-==-==-==-==-==-==-====-==-==')
print('       VOU PENSAR EM NÚMERO ENTRE 0 E 5. TENTE ADVINHAR EM QUAL NÚMERO PENSEI!')
print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-====-==-==-==-==-==-==-==-==-==-==-====-==-==')
user = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if user == think:
    print('Acertou Miseravi... Como sabia que eu estava pensando neste número?'.upper())
else:
    print('ERROOOOOOU!! Estava pensando no número {} e não no {}'.format(think,user))