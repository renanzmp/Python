#MEDIA 

n1 = float(input('Digite sua primeira nota:\n'))
while n1 <  0 or n1 > 10:
    print('Digite uma nota válida')
    n1 = float(input('Digite sua primeira nota:\n'))

n2 = float(input('Digite sua segunda nota:\n'))
while n2 < 0 or n2 > 10:
    print('Digite uma nota válida')
    n2 = float(input('Digite sua segunda nota:\n'))

media = (n1 + n2) / 2

if media < 5:
    print('Você obteve a média {:.2f}, por isso esta REPROVADO!'.format(media))
elif media >= 7:
    print('Você obteve a média {:.2f}, por isso está APROVADO!'.format(media))
else:
    print('Você obteve a média {:.2f}, por isso ficou de RECUPERAÇÃO!'.format(media))



    