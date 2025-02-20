#CONTANDO VOGAIS EM TUPLAS

tupla_palavras = ('irmao', 'ligar', 'geral', 'cobertor', 'lindo', 'cadela', 'escorpiao', 'amedrontar', 'teclado', 'arvore', 'cheque', 'mundo', 'terreno', 'carismatico', 'remedio', 'mercado', 'vasco', 'cerca', 'esquina', 'logica')

vogais = ""

for i in range(0, len(tupla_palavras)):
    if 'a' in tupla_palavras[i]:
        vogais = vogais + 'a '
    if 'e' in tupla_palavras[i]:
        vogais = vogais + 'e '
    if 'i' in tupla_palavras[i]:
        vogais = vogais + 'i '
    if 'o' in tupla_palavras[i]:
        vogais = vogais + 'o '
    if 'u' in tupla_palavras[i]:
        vogais = vogais + 'u '

    print(f'A palavra {tupla_palavras[i].upper()} contem as vogais: {vogais}')

    vogais = ""