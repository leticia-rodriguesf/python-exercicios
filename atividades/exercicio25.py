nome = str(input('Digite seu nome: '))
nome = nome.title().strip()
print('Seu nome tem silva? {}'.format_map('Silva' in nome))