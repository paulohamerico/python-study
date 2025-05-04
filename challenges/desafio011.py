l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ar = l*a
print('Sabendo que cada 1 litro de tinta é equivalente a 2m², com sua área de {}² você precisará de {:.1f} litros de tinta.'.format(ar,ar/2))
