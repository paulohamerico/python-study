#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

print('Vamos calcular o aumento no salário?')
sal = float(input('Digite o seu salário atual: R$'))
if sal <=1250:
    aumento = sal*0.15
else:
    aumento = sal*0.10
print('Você recebeu um aumento, agora seu salário é R${:.2f}.'.format(sal+aumento))
print('Que ótima noticia em?')
print('FIM')
