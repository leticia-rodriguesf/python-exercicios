frase = str(input('Digite alguma frase: ')).upper().strip()
print('A letra A aparece: {} vezes'.format(frase.count('A', 0)))
print('A primeria letra A apareceu na posição: {} '.format(frase.find('A')+1))
print('A última letra A apareceu na posição: {}'.format(frase.rfind('A')))