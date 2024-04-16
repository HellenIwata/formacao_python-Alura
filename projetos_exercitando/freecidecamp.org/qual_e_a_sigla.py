def msg_boas_vindas():
    '''
    Essa função é responsável por exibir a mensagem de boas vindas da aplicação.
    
    OUTPUT:
    Ao ser chamada, ela imprimirá na tela as BOAS VINDAS e uma breve explicação sobre a aplicação.
    '''
    print('****************************')
    print('Seja bem vindo ao programa!')
    print('****************************\n')
    print('Está aplicação verifica se o número digitado é PAR ou ÍMPAR\n')
    
def criacao_da_sigla():
    msg = input('Informe em uma frase em que você queira que ela vire uma sigla: \n')
    palavras = msg.split() #Função split(): separa a frase em palavras
    sigla = ''
    for palavra in palavras:
        sigla += palavra[0].upper() #palvra[0] pega apenas a primeira letra da palavra e .Upper() torna essa letra maiúscula
    print(f'Sua sigla ficou assim: {sigla}\n')
    nova_frase()

def nova_frase():
    nova_operacao = int(input('Gostaria de verificar outro número? \n 1 - Para Sim\n 2 - Para Não\n'))
    if nova_operacao == 1:
        criacao_da_sigla()
    else:
        print('\n*****************************')
        print('Obrigada por usar o programa!')
        print('*****************************\n')
        
def main():
    msg_boas_vindas()
    criacao_da_sigla()

if __name__ == "__main__":
    main()