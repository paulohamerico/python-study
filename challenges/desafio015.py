dias = int(input('Quantos dias você utilizou o carro: '))
km = float(input('Quantos KM você rodou com o carro: '))
valor = (dias*60)+(km*0.15)
print('O valor a ser pago é R${:.2f}.'.format(valor))

