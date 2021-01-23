from datetime import date
print('=-=-=-'*15)
print('                                  ALISTAMENTO OFICIAL    ')
print('=-=-=-'*15)
ano_nascimento = int(input('Qual é o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('--'*15)
print('Quem nasceu em {} tem {} anos de idade em {}'.format(ano_nascimento, idade, ano_atual))
if idade == 18:
    print('Já está na hora de se alistar!')
elif idade < 18:
    print('Você ainda irá se alistar')
    saldo = 18-idade
    print('Aproveite! Ainda falta {} anos'.format(saldo))
    alista = ano_atual + saldo
    print('Você irá se alistar em {}'.format(alista))
else:
    print('Já está meio velhinho, né?')
    print('Você já passou da hora de se alistar')
    saldo = idade - 18
    alista = ano_atual - saldo
    print('Já passou {} anos para se alistar'.format(saldo))
    print('Seu alistamento foi em {}'.format(alista))
