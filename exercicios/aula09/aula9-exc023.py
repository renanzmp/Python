#SEPARANDO DÍGITOS DE UM NÚMERO

numero = int(input('Digite um número de 0 à 9999\n'))

while(numero < 0 or numero > 9999):
    print('Digite um número válido!\n')
    numero = int(input('Digite um número de 0 à 9999\n'))

if(numero < 10):
    numero_txt = str(numero)
    print('unidade: {}'.format(numero_txt[0]))
elif(numero >= 10 and numero < 100):
    numero_txt = str(numero)
    print('unidade: {}'.format(numero_txt[1]))
    print('dezena: {}'.format(numero_txt[0]))
elif(numero >= 100 and numero < 1000):
    numero_txt = str(numero)
    print('unidade: {}'.format(numero_txt[2]))
    print('dezena: {}'.format(numero_txt[1]))
    print('centena: {}'.format(numero_txt[0]))
elif(numero >= 1000 and numero < 10000):
    numero_txt = str(numero)
    print('unidade: {}'.format(numero_txt[3]))
    print('dezena: {}'.format(numero_txt[2]))
    print('centena: {}'.format(numero_txt[1]))
    print('milhar: {}'.format(numero_txt[0]))
