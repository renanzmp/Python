from math import sqrt, floor
import emoji

print(emoji.emojize("Olá, mundo :globe_showing_americas:",  language='alias'))

num = int(input('Digite um número\n'))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, floor(raiz)))