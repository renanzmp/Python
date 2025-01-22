#AUMENTOS MÚLTIPLOS

salario = float(input('Digite o seu salário:\n'))

while salario <= 0:
    salario = float(input('Digite um salário válido:\n'))

if salario > 1250:
    aumento = (110/100) * salario
    print('Como o seu salário é superior à 1250 reais, você terá um aumento de 10%, sendo assim, seu salário a partir de agora será {} reais!'.format(aumento))
else:
    aumento = (115/100) * salario
    print('Como o seu salário é inferior ou igual à 1250 reais, você terá um aumento de 15%, sendo assim, seu salário a partir de agora será {} reais!'.format(aumento))
