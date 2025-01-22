#JOGO DE ADIVINHAÇÃO

import random

numero_certo = random.randint(1, 5)
numero = int(input('A máquina escolheu um número de 1 à 5, tente adivinhar:\n'))

while numero < 1 or numero > 5:
    print('Número inválido!\n')
    numero = int(input('Tente um número de 1 à 5!\n'))
    
if numero == numero_certo:
    print('Você acertou!!! O número sorteado era o {}'.format(numero_certo))
else:
    print('Você errou!!! O número sorteado era o {}, você escolheu o {}'.format(numero_certo, numero))
