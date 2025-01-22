nota1 = float(input('Digite a sua primeira nota\n'))
nota2 = float(input('Digite a sua segunda nota\n'))
media = (nota1 + nota2) / 2

print('Sua média é {:.1f}\n'.format(media))

if media >= 6:
    print('Você foi aprovado, muito bem!')
else:
    print('Você foi reprovado, estude mais!') 