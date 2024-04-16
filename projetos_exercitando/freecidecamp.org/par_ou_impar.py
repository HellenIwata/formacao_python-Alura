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

def verifica_o_numero():
    '''
    Está função é responsávle por  solicitar que o usuário digite um número e verificar se ele é PAR ou ÍMPAR.
    Aqui é feita a validação do número inserido pelo usuário. Caso ele seja um número onde o resto da divisão dele por "2" é "0" então o número é PAR, se o resto da divisão for diferente de "0" então o número é Ímpar.
    
    INPUT:
    numero: recebe o valor digitado pelo usuário.
    
    OUTPUT:
    Resultado da verificação e chamada para verificar uma nova operação de acordo com as escolhas do usuário.
    '''
    numero = int(input('Em qual número você pensou? '))
    verificador = numero % 2 # realiza a operação para verificar o resto da divisão 
    #Se o resto da divisão por 2 for igual a zero, é par. Senão é impar.
    if verificador == 0:
        print(f'Esse número ({numero}) é PAR!\n')
        nova_verificacao()
    else:
        print(f'Esse número ({numero}) é IMPAR!\n')
        nova_verificacao()

def nova_verificacao():
    '''
    Esta função é responsável por verificar uma nova operação de acordo  com as escolhas do usuário.
    
    INPUT:
    nova_operacao: recebe  a escolha do usuário para continuar ou parar a aplicação
    
    OUTPUT:
    Seus resultados e chamada recursiva caso deseje continuar
    O encerramento da aplicação se "2" for digitado
    '''
    nova_operacao = int(input('Gostaria de verificar outro número? \n 1 - Para Sim\n 2 - Para Não\n'))
    if nova_operacao == 1:
        verifica_o_numero()
    else:
        print('\n*****************************')
        print('Obrigada por usar o programa!')
        print('*****************************\n')
        
def main():
    msg_boas_vindas()
    verifica_o_numero()

if __name__ == "__main__":
    main()