nome = input('Qual é o seu nome? ')
while nome == '*':
    print('Você não digitou nenhum nome.\n')
    nome = input('Digite um nome válido.')
    
data_nascimento = input('Informe a sua data de nascimento: ')
endereco = input('Informe o endereço: ')
objetivos  = input('O que você quer alcançar com essa jornada?')
    
print(f'\n Nome: {nome}\n Data de nascimento: {data_nascimento}\n Endereço: {endereco}\n Objetivos: {objetivos}')