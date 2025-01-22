#RADAR ELETRÔNICO

limite = 80
vel = float(input('Digite a velocidade do seu carro em km/h:\n'))

while vel <= 0:
    print('Digite uma valocidade válida!\n')
    vel = float(input('Digite a velocidade do seu carro em km/h:\n'))
if vel <= 80:
    print('Você está dentro do limite de velocidade, continue assim!')
else:
    adicional = (vel - 80) * 7
    print('Você Está andando à {:.2f}km/h e ultrapassou o limite de velocidade! Por isso, você irá pagar uma multa de {:.2f} reais'.format(vel, adicional))


