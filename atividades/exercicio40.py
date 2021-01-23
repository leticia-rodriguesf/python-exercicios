parcial = float(input('Digite a nota de sua AV1: '))
bimestral = float(input('Digite a nota de sua AV2: '))
media = (parcial + bimestral)/2
if media < 5:
    print('REPROVADO')
    print('Com notas de {:.1f} e {:.1f}, sua média é de {:.2f}!'.format(parcial, bimestral,media))
elif (media == 5) and (media < 6.9):
    print('RECUPERAÇÃO')
    print('Com notas de {:.1f} e {:.1f}, sua média é de {:.2f}!'.format(parcial, bimestral, media))
else:
    print('APROVADO!')
    print('Com notas de {:.1f} e {:.1f}, sua média é de {:.2f}!'.format(parcial, bimestral, media))