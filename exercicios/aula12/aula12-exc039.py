#ALISTAMENTO MILITAR
import datetime

ano = datetime.date.today().year
nascimento = int(input('Digite seu ano de nascimento:\n'))
idade = ano - nascimento
tempo_menor = 18 - idade
tempo_maior = idade - 18

if idade < 18 and tempo_menor == 1:
    print('Ainda falta {} ano para você se alistar'.format(tempo_menor))
elif idade < 18 and tempo_menor != 1:
    print('Ainda faltam {} anos para você se alistar'.format(tempo_menor))
elif idade > 18 and tempo_maior == 1:
    print('Você deveria ter se alistado há {} ano'.format(tempo_maior))
elif idade > 18 and tempo_maior != 1:
    print('Você deveria ter se alistado há {} anos'.format(tempo_maior))
else:
    print('O ano para você se alistar é o ano atual')
