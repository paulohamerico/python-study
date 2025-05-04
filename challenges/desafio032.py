#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
from time import sleep
ano = int(input('Digite o ano para iniciar a verificação: '))
if ano == 0:
    ano = date.today().year
print('Verificando...')
sleep(1)
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
print('FIM')
