#SENO COSSENO TANGENTE
import math

angulo = int(input('Digite o valor de um angulo em graus\n'))

rad = math.radians(angulo)

sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O valor do seno, cosseno e tangente do ângulo {}° são, respectivamente {:.2f}, {:.2f}, {:.2f}'.format(angulo, sin, cos, tan))