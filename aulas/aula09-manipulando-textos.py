frase = "Oi, me chamo Renan e tenho 19 anos de idade!"

print(frase[9])
print(frase[4:12])
print(frase[7::2])
print(len(frase))
print(frase.count('e'))
print(frase.count('e', 0, 15))
print(frase.find('chamo'))
print('curso' in frase)
print('Renan' in frase)
print(frase.replace('Renan', 'Caio'))
print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print(frase.title())

frase2 = "  Estou aprendendo Python   "

print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

frase3 = 'Renan está aprendendo Python'
txt = frase3.split()
print(txt[1] [3])

print('-'.join(txt))
