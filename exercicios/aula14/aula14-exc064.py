#TRATANDO VÁRIOS VALORES v1.0

soma = 0
contagem = 0
print('Vamos pedir para você digitar quantos números vc quiser, quando quiser parar, digite 999')
num = int(input('Digite um número:\n'))

while num != 999:
    soma = soma + num
    contagem += 1
    num = int(input('Digite um número:\n'))

print(f'Você digitou {contagem} números, que somados dão {soma}')

    
