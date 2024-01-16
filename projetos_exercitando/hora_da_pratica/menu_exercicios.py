import funcao_print, condicionais, lista_for_try_except, dicionarios, os

def exibe_msg_abertura():
    print('''
        Exᴇʀᴄɪ́ᴄɪᴏs ʀᴇsᴏʟᴠɪᴅᴏs ᴅᴇ Pʏᴛʜᴏɴ
    ''')
    print('Os exercícios foram realizados durante o curso de Python: crie a sua primeira aplicação disponibilizado pela Alura')
    print('Caso tenha interesse em ver o funcionamento dos exercícios, escolha no menu')
    
def exibe_menu_escolha():
    
    print('''
        1. Exercícios da função print
        2. Exercícios de condicionais
        3. Exercícios de lista, laço de repetição for e try_except
    ''')

def escolher_opcao():
    try:
        escolha_opcao = int(input('Digite a opção desejada: '))
        
        if escolha_opcao == 1:
            funcao_print.executar_exercicios()
        elif escolha_opcao == 2:
            condicionais.executar_exercicios()
        elif escolha_opcao == 3:
            lista_for_try_except.executar_exercicios()
        else:
            input('Opção inválida, aperte qualquer tecla para voltar ao menu anterior')
            voltar_ao_menu()
    except:
        input('Opção inválida, aperte qualquer tecla para voltar ao menu anterior')
        voltar_ao_menu()

def voltar_ao_menu():
    os.system('cls')
    exibe_menu_escolha()
    escolher_opcao()


def menu_exercicios():
    exibe_msg_abertura()
    exibe_menu_escolha()
    escolher_opcao()


            
            
            
if __name__ == '__main__':
    menu_exercicios()