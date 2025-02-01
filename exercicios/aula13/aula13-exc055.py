#MAIOR E MENOR DA SEQUÊNCIA

lista_pesos = []

for i in range(1, 6):
    pesos = float(input('{}° pessoa, digite seu peso:\n'.format(i)))
    while pesos <= 0:
        print('Digite um peso válido')
        pesos = float(input('{}° pessoa, digite seu peso:\n'.format(i)))
    lista_pesos.append(pesos)

menor_peso = min(lista_pesos)
maior_peso = max(lista_pesos)

print('O menor peso é {:.2f} e o maior peso é {:.2f}'.format(menor_peso, maior_peso))