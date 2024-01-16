def executar_exercicios():
        #1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
    print('''
    É PAR OU ÍMPAR?
    ''')
    numero = int(input('Digite um número: '))
    resto_da_divisao = numero % 2

    if resto_da_divisao == 0:
        print(f'O número {numero} é par\n')
    else:
        print(f'O número {numero} é ímpar\n')

    #2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições: Criança: 0 a 12 anos; Adolescente: 13 a 18 anos; Adulto: acima de 18 anos.
    print('''
    ADULTO, ADOLESCENTE OU CRIANÇA?
    ''')
    idade = int(input('Digite sua idade para a verificação: '))

    if idade >= 0 and idade <= 12:
        print('Você é uma criança\n')
    elif idade >= 13 and idade <= 18:
        print('Você é um adolescente\n')
    else:
        print('Você é um adulto\n')

    #3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
    print('''
    VALIDAÇÃO DE USUÁRIO E SENHA
    ''')
    usuario = input('Informe um nome de usuário: ')
    senha = input('Digite uma senha: ')

    usuario_acesso = 'alura.python'
    senha_acesso = 'python3@alura'

    if usuario == usuario_acesso and senha == senha_acesso:
        print('Login efetuado')
    else:
        print('Parece que houve um problema... o usuário ou senha são inválidos')

    #4-Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições: Primeiro Quadrante: os valores de x e y devem ser maiores que zero; Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero; Terceiro Quadrante: os valores de x e y devem ser menores que zero; Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero; Caso contrário: o ponto está localizado no eixo ou origem.
    print('''
    VALIDAÇÃO QUADRANTE DO PLANO CARTESIANO
    ''')

    valor_de_x = float(input('Informe o valor de X: '))
    valor_de_y = float(input('Informe o valor de Y: '))

    if valor_de_x > 0 and valor_de_y > 0:
        print('O ponto se encontra no 1º quadrante do plano.')
    elif valor_de_x < 0 and valor_de_y > 0:
        print('O ponto se encontra no 2º quadrante do plano.')
    elif valor_de_x < 0 and valor_de_y < 0:
        print('O ponto se encontra no 3º quadrante do plano.')
    elif valor_de_x > 0 and valor_de_y < 0:
        print('O ponto se encontra no 4º quadrante do plano.')
    else:
        print('O ponto está localizado no eixo ou origem.')
        
if __name__ == '__main__':
    executar_exercicios()