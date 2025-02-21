num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2)
num.sort(reverse=True)
num.pop(2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'A lista tem {len(num)} elementos')

for c, i in enumerate(num):
    print(f'na posição {c}, encontrei o valor {i}!')

'''lista_numeros = []

for cont in range (0, 5):
    lista_numeros.append(int(input('Digite um número: ')))

print(lista_numeros)'''

lista_a = [5, 3, 9, 2]
# LIGA UMA LISTA À OUTRA
# lista_b = lista_a
lista_b = lista_a[:]
lista_b.append(0)

print(f'Lista A: {lista_a}')
print(f'Lista B {lista_b}')


listaaa = [3, 4, 8, 1 , 5]
listaaa.insert(2, 11)
print(listaaa)