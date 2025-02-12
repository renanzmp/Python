#SIMULADOR DE CAIXA ELETRÔNICO

notas_de_cinquenta = 0
notas_de_vinte = 0
notas_de_dez = 0
notas_de_um = 0

valor = int(input('Quanto você quer sacar? R$'))
while valor >= 5000 or valor < 1:
    print('Digite um valor maior do que R$0 até R$5000')
    valor = int(input('Quanto você quer sacar? R$'))

if valor >= 50:
    notas_de_cinquenta = valor // 50
    resto = valor % 50
    if resto != 0:
        if resto >= 20:
            notas_de_vinte = resto / 20
            resto = resto % 20
            if resto >= 10:
                notas_de_dez = resto / 10
                resto = resto % 10
                if resto >= 1:
                    notas_de_um = resto / 1
        if resto >= 10:
                notas_de_dez = resto / 10
                resto = resto % 10
                if resto >= 1:
                    notas_de_um = resto / 1
        if resto >= 1:
                    notas_de_um = resto / 1
elif valor >= 20:
    notas_de_vinte = valor // 20
    resto = valor % 20
    if resto != 0:
        if resto >= 10:
            notas_de_dez = resto / 10
            resto = resto % 10
        if resto >= 1:
                notas_de_um = resto / 1
                resto = resto % 1
elif valor >= 10:
    notas_de_dez = valor // 10
    resto = valor % 10
    if resto != 0:
        if resto >= 1:
            notas_de_um = resto / 1
            resto = resto % 1
elif valor >= 1:
    notas_de_um = valor // 1
    resto = valor % 1
              
          
            

if notas_de_cinquenta != 0:
     print(f'{notas_de_cinquenta} notas de cinquenta')
if notas_de_vinte != 0:
     print(f'{int(notas_de_vinte)} notas de vinte')
if notas_de_dez != 0:
     print(f'{int(notas_de_dez)} notas de 10')
if notas_de_um != 0:
     print(f'{int(notas_de_um)} notas de 1')
    