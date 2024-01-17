import os

restaurantes = [{'nome':'Iwata Sushi','categoria':'Japonesa','ativo':False},
                {'nome':'RufPizzas','categoria':'Italiana','ativo':True},
                {'nome':'Bar e restaurante do Jorge','categoria':'Brasileira','ativo':False}]

def exibir_nome_do_programa():
    '''
        Esta função é responsável por exibir o nome da aplicação
        
        OUTPUTS:
        - Saída do nome da aplicação
    '''
    print(""" 
        丂闩⻏ㄖ尺   㠪〤尸尺🝗丂丂
    """)

def exibir_menu_de_opcoes():
    '''
        Esta função é responsável por listar o menu de escolhas
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair \n')

def opcao_invalida():
    '''Esta função é responsável exibir a mensagem quando a opção for inválida'''
    print('ERRO!!! Opção inválida')
    voltar_ao_menu_principal()
    
def escolher_opcao():
    '''
        Esta função é responsável por realizar a condicional para a escolha de opções
        
        INPUT:
        - Opção escolhida
        
        OUTPUT:
        - Direciona para o menu escolhido
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            listar_restaurante()
            
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
            
        elif opcao_escolhida == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def voltar_ao_menu_principal():
    '''
        Esta função é responsável por retornar ao menu principal
        
        INPUT:
        - Recebe a escolha do usuário voltar ao menu ou encerrar o app
        
        OUTPUT:
        - 1 selecionado volta ao menu principal
        - 0 selecionado encerra o app
    '''
    voltar = int(input('\n \n Digite 1 para retornar ao menu principal ou 0 para encerrar o app: '))
    if voltar == 1:
        main()
    else:
        encerrar_app()
    
def exibir_subtitulos(texto):
    '''
        Esta função é responsável por exibir os substitulos de cada opção do app
        
        INPUT:
        - texto: str - Exibe o texto do subtitulo
    '''
    os.system('cls')
    borda = '*' * (len(texto) + 4)
    print(borda)
    print(texto)
    print(borda)
    print('\n')

def cadastrar_novo_restaurante():
    '''
        Esta função é responsável por cadastrar um novo restaurante
        
        INPUTS:
        - Nome do novo restaurante
        - Categoria do novo restaurante
        
        OUTPUTS:
        - Adiciona o novo restaurante a lista
    '''
    exibir_subtitulos('Cadastro de novos Restaurante')
    
    novo_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do {novo_restaurante}: ')
    dados_restaurantes = [{'nome':novo_restaurante, 'categoria':categoria} ]
    restaurantes.append(dados_restaurantes) 
    
    print(f'{novo_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    '''
        Esta função é responsável por realizar a listagem dos restaurantes
        
        OUTPUT:
        - Exibe a lista de restaurantes
    '''
    exibir_subtitulos('Listagem de Restaurante')
    
    print(f'{'Restaurante'.lsjust(22)} | {'Categoria'.lsjust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f'- {nome_restaurante.lsjust(20)} | {categoria.lsjust(20)} | {ativo}')
    
    #voltar_ao_menu_principal()       

def alterar_status_restaurante():
    '''
        Esta função é responsável por alterar o status dos restaurantes
        
        INPUT:
        - Nome do restaurante
        
        OUTPUT:
        - Alteração do status do restaurante
        - Exibição da mensagem indicando se houve sucesso ou falha
    '''
    exibir_subtitulos('Alteração do status do Restaurante')
    
    nome_restaurante= input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_localizado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_localizado = False
            restaurante['ativo'] = not restaurante ['ativo']
            msg = f'O {nome_restaurante} foi ativado com suceso!' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado com sucesso!'
            print(msg)
    
    if not restaurante_localizado:
        print(f'ERRO! O {nome_restaurante} não foi localizado')
            
    voltar_ao_menu_principal()

def encerrar_app():
    exibir_subtitulos('Obrigada por usar! \nEncerrando o aplicativo')

def main():
    '''
        Função principal responsável por iniciar o programa
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu_de_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()