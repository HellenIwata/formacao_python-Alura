def msg_boas_vindas():
    '''
    Essa função é responsável por exibir a mensagem de boas vindas da aplicação.
    
    OUTPUT:
    Ao ser chamada, ela imprimirá na tela as BOAS VINDAS e uma breve explicação sobre a aplicação.
    '''
    
    print('***************************')
    print('Seja bem vindo ao programa!')
    print('***************************\n')
    print('Esta aplicação é capaz de receber uma frase que você digitar e contabilizar quantas palavras são usadas nesta frase.')

def leitura_dados():
    '''
    Esta função é responsável por receber a frase que o usuário gostaria de realizar a contagem das palavras. 
    
    INPUT:
    msg: recebe a frase que o usuário deseja contabilizar as palavras
    
    OUTPUT:
    contagem_palavras: realiza a contagem das palavras na frase digitada pelo usuário
    Imprime a mensagem informando quantas palavras foram usadas na frase.
    '''
    
    msg = input('Informe em uma frase algo em que você pensou hoje. \n')
    palavras = msg.split()
    
    contagem_palavras = len(palavras)        
    print(f'Legal! Você acabou de me dizer no que pensou usando {contagem_palavras} palavras.\n')
    
    nova_contagem()
    
def nova_contagem():
    nova_operacao = int(input('Gostaria de verificar outro número? \n 1 - Para Sim\n 2 - Para Não\n'))
    if nova_operacao == 1:
        leitura_dados()
    else:
        print('\n*****************************')
        print('Obrigada por usar o programa!')
        print('*****************************\n')
        
def main():
    msg_boas_vindas()
    leitura_dados()

if __name__ == "__main__":
    main()