#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, inde de 10 até 0, com uma pause de 1 segundo entre eles.

from time import sleep

print('Vamos iniciar a contagem dos fogos! Se prepare!')
sleep(1)
for c in range(10, -1, -1):
    if c < 10:
        sleep(1)
    print(c)
print('FELIZ ANO NOVOOOOOO!!!')
print('(Onomatopeia de fogos estourando)')