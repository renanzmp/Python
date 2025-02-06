#JOGO DA ADIVINHAÇÃO v2.0

import random

numero_aleatorio = random.randint(1, 10)
numero_adivinhado = int(input('Digite um número para adivinhar:\n'))
tentativas = 1



while numero_adivinhado != numero_aleatorio:
    print('Você errou, tente novamente:')
    numero_adivinhado = int(input('Digite um número para adivinhar:\n'))
    tentativas += 1

print('Parabéns, você acertou! O número era {}!!!'.format(numero_aleatorio))
print('Você precisou de {} tentativas para adivinhar o número aleatório'.format(tentativas))
