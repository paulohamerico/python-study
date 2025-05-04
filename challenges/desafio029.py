#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada KM acima do limite.

vcarro = float(input('Qual a velocidade do carro? '))
multa = (vcarro - 80)*7
if vcarro > 80:
    print('MULTADO! O carro está acima do limite de velocidade!')
    print('Você receberá uma multa de R${:.2f} pelo excesso de velocidade!'.format(multa))
else:
    print('O carro está dentro do limite!')
print('FIM')
