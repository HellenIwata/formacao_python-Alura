from random import randint

def msg_boas_vindas():
    '''
    Essa função é responsável por exibir a mensagem de boas vindas da aplicação.
    
    OUTPUT:
    Ao ser chamada, ela imprimirá na tela as BOAS VINDAS e uma breve explicação sobre a aplicação.
    '''
    print('\n *' *25)
    print('Seja bem vindo a aplicação!')
    print('*' *25)
    print('Esta aplicação é um joguinho simples de Pedra, Papel e Tesoura, onde você joga contra o computador\n')
    

escolhas = ['pedra','tesoura',  'papel']
escolha_computador = escolhas[randint(0, 2)]

def exibir_opcao_escolha():
    print('''
        1 - Pedra
        2 - Tesoura
        3 - Papel
        ''')
    
escolha_usuario = int(input('Digite a sua escolha:'))

""" if escolha_usuario == escolha_computador:
    print(f'\nVocê jogou {escolha_usuario}!\nO computador jogou {escolha_computador}!\nEMPATE!')
    
elif escolha_usuario ==  'pedra' and escolha_computador == 'tesoura':
    print(f'\nVocê jogou {escolha_usuario}!\nO computador jogou {escolha_computador}\n VOCÊ GANHOU')
    
elif escolha_usuario == 'tesoura' and escolha_computador ==  'papel':
    print(f'\nVocê jogou {escolha_usuario}!\nO computador jogou {escolha_computador}\n VOCÊ GANHOU')
 """