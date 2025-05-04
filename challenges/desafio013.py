s = float(input('Digite seu salário atual: '))
a = float(input('Digite a porcentage do aumento: '))
cp = a/100
pa = s*cp
sf = s+pa
print('Como seu salario atual é R${}, considerando o aumento ficará R${}.'.format(s, sf))