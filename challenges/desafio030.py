#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

import math
numero = int(input('Digite um número para saber se ele é PAR ou ÍMPAR: '))
if numero % 2 == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))
print('FIM')
