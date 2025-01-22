#MENOR E MAIOR VALORES

num1 = int(input('Digite o 1° número\n'))
num2 = int(input('Digite o 2° número\n'))
num3 = int(input('Digite o 3° número\n'))

if num1 < num2 < num3:
    print('o {} é o maior número e o {} é o menor número'.format(num3, num1))
elif num1 < num3 < num2:
    print('o {} é o maior número e o {} é o menor número'.format(num2, num1))
elif num2 < num1 < num3:
    print('o {} é o maior número e o {} é o menor número'.format(num3, num2))
elif num2 < num3 < num1:
    print('o {} é o maior número e o {} é o menor número'.format(num1, num2))
elif num3 < num1 < num2:
    print('o {} é o maior número e o {} é o menor número'.format(num2, num3))
else:
    print('o {} é o maior número e o {} é o menor número'.format(num2, num1))