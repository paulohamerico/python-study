c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
#f = 9 * c / 5 + 32 -> Também pode ser utilizado sem os parenteses por conta da ordem de precedencia.
print('A temperatura de {0}ºC corresponde a {1}ºF!'.format(c, f))
