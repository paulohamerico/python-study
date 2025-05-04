#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.

print('Você vai fazer uma viagem? Vou ajudar a calcular o valor!')
dis = float(input('Quantos KM até o seu destino? '))
if dis <= 200:
    print('Certo, em uma viagem de {}Km você irá gastar R${:.2f}.'.format(dis, (dis *0.5)))
else:
    print('Certo, em uma viagem de {}Km você irá gastar R${:.2f}.'.format(dis, (dis* 0.45)))
print('Aproveite!')
print('FIM')

'''Poderia ter utilizado da seguinte forma:
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
    
Ter feito um unico print e o .format(preço)'''

