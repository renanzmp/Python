#SOMA DE ÍMPARES MULTIPLOS DE 3

s = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i

print(s)
