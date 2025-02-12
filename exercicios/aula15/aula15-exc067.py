#TABUADA v3.0

num = 0

while True:
    num = float(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
        
print('Programa encerrado!')