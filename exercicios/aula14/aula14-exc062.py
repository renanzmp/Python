#PROGRESSÃO ARITIMÉTICA v3.0

primeiro_termo = int(input('Digite o primeiro termo da P.A.:\n'))
razao = int(input('Digite a razão da P.A.:\n'))
termos = 1

print(primeiro_termo)

while termos < 10:
    primeiro_termo += razao
    termos +=1
    print(primeiro_termo)

termos_adicionais = int(input('Você quer mostrar mais quantos termos?\n'))

while termos_adicionais != 0:
    termos = 1
    while termos <= termos_adicionais:
        primeiro_termo += razao
        termos +=1
        print(primeiro_termo)
    termos_adicionais = int(input('Você quer mostrar mais quantos termos?\n'))

print('Fim do Programa')

