#PEDRA PAPEL OU TESOURA
from random import choice

lista_opcoes = ['pedra', 'papel', 'tesoura']
escolha_computador = choice(lista_opcoes)

escolha_jogador = int(input('Digite 1 para PEDRA;\nDigite 2 para PAPEL;\nDigite 3 para TESOURA;\n'))
while str(escolha_jogador) not in '1 2 3':
    print('Escolha uma opção válida')
    escolha_jogador = int(input('Digite 1 para PEDRA;\nDigite 2 para PAPEL;\nDigite 3 para TESOURA;\n'))

if escolha_jogador == 1 and escolha_computador == 'pedra':
    print('Você escolheu PEDRA e o computador escolheu {}. EMPATE'. format(escolha_computador.upper()))
elif escolha_jogador == 1 and escolha_computador == 'papel':
    print('Você escolheu PEDRA e o computador escolheu {}. VOCÊ PERDEU'. format(escolha_computador.upper()))
elif escolha_jogador == 1 and escolha_computador == 'tesoura':
    print('Você escolheu PEDRA e o computador escolheu {}. VOCÊ GANHOU'. format(escolha_computador.upper()))
elif escolha_jogador == 2 and escolha_computador == 'pedra':
    print('Você escolheu PAPEL e o computador escolheu {}. VOCÊ GANHOU'. format(escolha_computador.upper()))
elif escolha_jogador == 2 and escolha_computador == 'papel':
    print('Você escolheu PAPEL e o computador escolheu {}. EMPATE'. format(escolha_computador.upper()))
elif escolha_jogador == 2 and escolha_computador == 'tesoura':
    print('Você escolheu PAPEL e o computador escolheu {}. VOCÊ PERDEU'. format(escolha_computador.upper()))
elif escolha_jogador == 3 and escolha_computador == 'pedra':
    print('Você escolheu TESOURA e o computador escolheu {}. VOCÊ PERDEU'. format(escolha_computador.upper()))
elif escolha_jogador == 3 and escolha_computador == 'papel':
    print('Você escolheu TESOURA e o computador escolheu {}. VOCÊ GANHOU'. format(escolha_computador.upper()))
elif escolha_jogador == 3 and escolha_computador == 'tesoura':
    print('Você escolheu TESOURA e o computador escolheu {}. EMPATE'. format(escolha_computador.upper()))
else:
    print('deu ruim')