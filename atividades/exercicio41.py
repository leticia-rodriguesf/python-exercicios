from datetime import date
print('--'*25)
print('        CONFEDERAÇÃO NACIONAL DE NATAÇÃO    ')
print('--'*25)
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano_nascimento
print('O atleta tem {} anos'.format(idade))
if idade <=  9:
    print('A sua categoria é MIRIM')
elif idade <= 14:
    print('A sua categoria é INFANTIL')
elif idade <= 19:
    print('A sua categoria é JUNIOR')
elif idade <= 25:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')