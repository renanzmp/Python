#ANALISANDO TRIANGULO v1

lado1 = int(input('Digite o 1° lado do triangulo:\n'))
while lado1 <= 0:
    lado1 = int(input('Digite um valor válido:\n'))
lado2 = int(input('Digite o 2° lado do triangulo:\n'))
while lado2 <= 0:
    lado2 = int(input('Digite um valor válido:\n'))
lado3 = int(input('Digite o 3° lado do triangulo:\n'))
while lado3 <= 0:
    lado3 = int(input('Digite um valor válido:\n'))

if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
    print('O triângulo de lados {}, {} e {} não pode ser criado'.format(lado1, lado2, lado3))
else:
    print('Esse triangulo é válido!')


