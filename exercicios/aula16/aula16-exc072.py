#NÚMERO POR EXTENSO

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 à 20:\n'))

while num < 0 or num > 20:
    num = int(input('Número inválido. Digite um número de 0 à 20:\n'))

print(numeros[num])