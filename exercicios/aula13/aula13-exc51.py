#PROGRESSÃO ARITIMÉTICA

primeiro_termo = int(input('Digite o primeiro termo da sua P.A.:\n'))
razao = int(input('Digite a razão da sua P.A.:'))

for i in range(primeiro_termo, (razao*10) + primeiro_termo , razao):
    print(i)