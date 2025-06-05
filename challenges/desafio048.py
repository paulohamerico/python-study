#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
from time import sleep

print('Iniciando Programa...')
r = 0
for c in range (1, 501):
   if c % 3 == 0 and c % 2 != 0:
       r = r + c
sleep(1)
print('Quase lá...')
sleep(1)
print(f'O Resultado do calculo é {r}.')
