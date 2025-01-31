#CLASSIFICANDO ATLETAS
import datetime

ano = datetime.date.today().year
nascimento = int(input('Digite o seu ano de nascimento\n'))
idade = ano - nascimento

if idade < 6:
    print('Não cadastramos atletas com essa idade')
elif idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
