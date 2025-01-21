#SORTEANDO UMA ORDEM NA LISTA
import random

nome1 = str(input('Primeiro aluno\n'))
nome2 = str(input('Segundo aluno\n'))
nome3 = str(input('Terceiro aluno\n'))
nome4 = str(input('Quarto aluno\n'))

alunos = [nome1, nome2, nome3, nome4]

print('Os alunos do grupo são {},'.format(alunos), end=' ')

random.shuffle(alunos)

print('a ordem da apresentação será {}'.format(alunos))