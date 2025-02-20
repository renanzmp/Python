#LISTA DE PREÇOS COM TUPLA

tupla_produtos = ('Pão Francês', 1, 'Queijo Kg', 49.90, 'Mortadela Kg', 40.99, 'Sonho', 4.50, 'Presunto', 37, 'Pão de Forma', 9.50)


for i in range(0, len(tupla_produtos), 2):
    print(f'{tupla_produtos[i]} -------------------------- R${tupla_produtos[i+1]:.2f}')