#PALÍNDROMO

frase = str(input('Digite uma frase qualquer e veremos se ela é um palíndromo:\n'))
frase_sem_espacos = frase.replace(" ", "")
invertida = "".join(frase[::-1])
invertida_sem_espacos = invertida.replace(" ", "")

if frase_sem_espacos == invertida_sem_espacos:
    print('A frase {} ao contrário é {}. É UM palíndromo'.format(frase, invertida))
else:
    print('A frase {} ao contrário é {}. NÃO É um palíndromo'.format(frase, invertida))