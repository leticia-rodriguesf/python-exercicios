print('==='*30)
print('                    SORTEIO DE EQUIPES                      ')
print('==='*30)
from random import shuffle
equipe1 = input('Primeiro aluno: ')
equipe2 = input('Segundo aluno: ')
equipe3 = input('Terceiro aluno: ')
equipe4 = input('Quarto aluno: ')
lista = [equipe1, equipe2, equipe3, equipe4]
shuffle(lista)
print('A ordem de apresentação é: ', lista)
print('==='*30)