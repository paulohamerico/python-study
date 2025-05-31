#Refaça o Desafio 032 dos triângulos, acrescentando o recurso de motrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isosceles dois lados iguais
#Escaleno todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triangulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos NÃO PODEM formar um triangulo!')
