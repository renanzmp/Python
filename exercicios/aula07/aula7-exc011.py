#PINTANDO PAREDE

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

while largura <= 0 or altura <= 0:

    print('Digite números válidos')
    largura = float(input('Digite a largura da parede'))
    altura = float(input('Digite a altura da parede'))

area = altura * largura

tinta = area/2

print('A sua parede tem mede {}m², dito isso, você precisaria de {} litros de tinta para conseguir pintá-la por completo' .format(area, tinta))