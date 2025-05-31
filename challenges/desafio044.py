#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#A vista dinheiro/cheque: 10% de desconto
#A vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('Vamos verificar o valor final do produto escolhido.')
nomep = str(input('Digite o nome do produto: '))
preço = float(input('Digite o valor do produto: R$ '))
mp = int(input('Escolha o método de pagamento. \n Digite 1 para pagamento a vista com dinheiro/PIX. \n Digite 2 para pagamento a vista com cartão. \n Digite 3 para pagamento em até 2x no cartão. \n Digite 4 para pagamento 3x ou mais no cartão. \n Opção escolhida: '))
if mp == 1:
    mp = 'a vista com dinheiro/PIX'
    print(f'{nomep} custa R$ {preço:.2f} e o pagamento escolhido foi {mp}.')
    print(f'Você ganhou 10% de desconto, então deve pagar R$ {preço-(preço*10/100):.2f}.')
elif mp == 2:
    mp = 'a vista no cartão'
    print(f'{nomep} custa R$ custa R$ {preço:.2f} e o pagamento escolhido foi {mp}.')
    print(f'Você ganhou 5% de desconto, então deve pagar R$ {preço-(preço*5/100):.2f}.')
elif mp == 3:
    mp = f'em 2x de R${preço / 2:.2f} no cartão'
    print(f'{nomep} custa R$ {preço:.2f} e o pagamento escolhido foi {mp}.')
    print(f'Não houve desconto com o método escolhido, então deve considerar R$ {preço:.2f}.')
elif mp == 4:
    totalp = int(input('Quantas parcelas serão? '))
    mp = f'em {totalp}x de R${preço / totalp:.2f}'
    print(f'{nomep} custa R$ {preço:.2f} e o pagamento escolhido foi {mp}.')
    print(f'Será considerado 20% de juros, então o valor a ser pago é R$ {preço+(preço*20/100):.2f}.')
else:
    print('Método de pagamento invalido! Você precisa escolher uma opção apenas entre 1 e 4.')
