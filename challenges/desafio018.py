from math import radians, cos, sin, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo {} tem o SENO de {:.2f}.'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE {:.2f}.'.format(angulo, tangente))
