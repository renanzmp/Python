#PAR OU ÍMPAR

import random

venceu = 0

while True:
    numero_aleatorio = random.randint(1, 10)
    par_ou_impar = str(input('Par ou Impar? [P/I]\n')).upper()
    while True:
        if par_ou_impar in ['P', 'I']:
            break
        print('Digite uma opão válida')
        par_ou_impar = str(input('Par ou Impar? [P/I]\n'))
    numero_escolhido = int(input('Digite um número:\n'))
    soma = numero_aleatorio + numero_escolhido
    if par_ou_impar == 'P' and soma % 2 == 0:
        print(f'Você jogou {numero_escolhido} e o computador {numero_aleatorio}. Total de {soma}. Deu PAR.\nVamos jogar novamente')
        venceu += 1
    elif par_ou_impar == 'I' and soma % 2 == 1:
        print(f'Você jogou {numero_escolhido} e o computador {numero_aleatorio}. Total de {soma}. Deu IMPAR.\nVamos jogar novamente')
        venceu += 1
    elif par_ou_impar == 'P' and soma % 2 == 1:
        print(f'Você jogou {numero_escolhido} e o computador {numero_aleatorio}. Total de {soma}. Deu IMPAR.\nVocê perdeu!\nVocê ganhou {venceu} vezes!')
        break
    elif par_ou_impar == 'I' and soma % 2 == 0:
        print(f'Você jogou {numero_escolhido} e o computador {numero_aleatorio}. Total de {soma}. Deu PAR.\nVocê perdeu!\nVocê ganhou {venceu} vezes!')
        break
        