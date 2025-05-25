#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.

casa = float(input('Qual o valor do imovel? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos será pago? '))

meses = anos * 12
prestacao = casa/meses
limite = salario * 0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos ({} meses)'.format(casa, anos, meses))
print('A prestação será de R$ {:.2f}'.format(prestacao))

if prestacao > limite:
    print('Emprestimo NEGADO: A prestação excede 30% do salário.')
else:
    print('Emprestimo APROVADO!')
