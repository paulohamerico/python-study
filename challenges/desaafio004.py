a = input('Digite algo: ')
print('O tipo primitivo inserido é', type(a))
print('Só tem espaços?', a.isspace())
print('Éa apenas numerico?', a.isnumeric())
print('É apenas alfabetico?', a.isalpha())
#print('É alfanumerico?', a.isalnum())
print('É alfanumerio? {}'.format(a.isalnum()))

