#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

nome = str(input('Digite o nome de uma cidade: ')).strip()
verifica = 'SANTO' in nome.upper().split()[0]
print('O nome da cidade começa com "Santo"?\n{} '.format(verifica))
