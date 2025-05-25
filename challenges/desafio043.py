#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso ideal
#25 até o 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida

print('Vamos calcular seu IMC e entender como você está em relação ao seu peso ideal.')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC hoje é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal.')
elif imc >=25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com Obesidade.')
else:
    print('Você está com Obesidade mórbida.')
