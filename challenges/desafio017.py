'''co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {}.'.format(hi))'''

#-------------------------

'''from math import pow, sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = pow(co, 2) + pow(ca, 2)
print('Com base no cateto oposto {} e cateto adjacente {} a é hipotenusa {:.2f}'.format(co, ca, sqrt(hi)))'''

#-------------------------

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


