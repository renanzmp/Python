#CUSTO DA VIAGEM

print('Iremos calcular o valor da sua viagem conforme a distância.')
distancia = int(input('Digite a distância em Km:\n'))

while distancia <= 0:
    print('Coloque uma distância válida!')
    distancia = int(input('Digite a distância em Km:\n'))

preco1 = distancia * 0.5
preco2 = distancia * 0.45

if distancia <= 200:
    print('Como a sua viagem é curta, o preço será {} reais'.format(preco1))
else:
    preco = distancia * 0.45
    print('Como a sua viagem é longa, o preço será {} reais ao invés de {} reais'.format(preco2, preco1))
