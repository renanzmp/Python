#CALCULADOR DO ÍNDICE DE MASSA CORPORAL

peso = float(input('Nos informe o seu peso em Kg (Ex: 80):\n'))
while peso < 0:
    print('Digite um peso válido!')
    peso = float(input('Nos informe o seu peso em Kg (Ex: 80):\n'))
    
altura_centimetro = float(input('Nos informe sua altura (Ex: 180):\n'))
while altura_centimetro < 0:
    print('Digite uma altura válida!')
    altura_centimetro = float(input('Nos informe sua altura em cm (Ex: 180):\n'))

altura = altura_centimetro / 100

imc = peso / (altura * altura)

if imc < 18.5:
    ('Você está com o IMC DE {:.2f}. Você está abaixo do peso!'.format(imc))
elif imc < 25:
    print('Você está com o IMC DE {:.2f} .Você está no peso ideal!'.format(imc))
elif imc < 30:
    print('Você está com o IMC DE {:.2f} .Você está em SOBREPESO!'.format(imc))
elif imc < 40:
    print('Você está com o IMC DE {:.2f} .Você está OBESO!'.format(imc))
else:
    print('Você está com o IMC DE {:.2f} .Você está com OBESIDADE MÓRBIDA!'.format(imc))