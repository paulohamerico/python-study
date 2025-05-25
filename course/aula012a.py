nome = str(input('Qual é seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome =='Geovana' or nome == 'Andrea':
    print('Seu nome é bem popular por aqui em!')
elif nome in 'Ana Cláduia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))
