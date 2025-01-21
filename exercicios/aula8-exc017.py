#CATETOS E HIPOTENUSA
from math import sqrt, pow

cat1 = float(input('Digite um valor para o cateto 1\n'))
while cat1 <= 0:
    cat1 = float(input('Valor inválido! Digite um número maior do que 0\n'))

cat2 = float(input('Digite um valor para o cateto 2\n'))
while cat2 <= 0:
    cat2 = float(input('Valor inválido! Digite um número maior do que 0\n'))

hip = sqrt(pow(cat1, 2) + pow(cat2, 2))  
print(hip)  
