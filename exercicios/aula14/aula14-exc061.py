#PROGRESSÃO ARITIMÉTICA v2.0

primeiro_termo = int(input('Digite o primeiro termo da P.A.:\n'))
razao = int(input('Digite a razão da P.A.:\n'))
termos = 1

print(primeiro_termo)

while termos < 10:
    primeiro_termo += razao
    termos +=1
    print(primeiro_termo)