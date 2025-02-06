#SEQUENCIA DE FIBONACCI

n = int(input('Digite quantos termos você quer mostrar:\n'))
t1 = 0
t2 = 1
t3 = 0
contador = 3

print(f'{t1} - {t2}', end=" - ")

while contador <= n:
    t3 = t1 + t2
    print(f'{t3}', end=" - ")
    contador += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2

print('FIM')