# biblioteca importada para sortear os números aleatórios do jogo
import random
import menu_jogos

from forca import imprime_mesagem_fim_jogo


def jogar():
    imprime_msg_abertura()

    num_secreto = random.randrange(1, 101)  # Definindo quais números podem ser escolhidos para ser o secreto (entre 1 e 100)
    #total_de_tentativas = 0
    pontos = 1000

    # Criando o nível de dificuldade do jogo
    imprime_nivel_jogo()
    nivel = int(input("Digite a opção desejada: "))
    print(end="\n\n")

    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Iniciando a sequencia do jogo
    condicao_para_o_jogo(total_de_tentativas, num_secreto, pontos)

    jogar_novamente = input('Deseja jogar novamente? s/n ')
    if jogar_novamente == 'n':
        imprime_mesagem_fim_jogo()
        voltar_ao_menu()
    else:
        jogar()


def imprime_msg_abertura():
    print("*************************************")
    print("******* *Jogo de Adivinhação* *******")
    print("*************************************", end="\n\n")


def imprime_nivel_jogo():
    print("********* *Escolha a dificuldade:* *********")
    print("********************************************", end="\n")
    print('(1) Fácil | (2) Intermediário | (3) Difícil')
    print("********************************************", end="\n")


def condicao_para_o_jogo(total_de_tentativas, num_secreto, pontos):
    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

        chute_str = input('Digite um número entre 1 e 100: ')
        print('O número escolhido foi: ', chute_str)
        num_chute = int(chute_str)

        # Criando regras para que o jogo aceite apenas números entre 1 e 100
        if num_chute < 1 or num_chute > 100:
            print('!!! *Número inválido* !!!', end='\n')
            print('Digite um número entre 1 e 100')
            continue

        # Criando as dicas para o jogo
        acertou = num_chute == num_secreto
        maior = num_chute > num_secreto
        menor = num_chute < num_secreto

        # Criando a condição para a dica
        if acertou:
            print('Parabéns, você acertou!', end='\n')
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ", end='\n\n')
            print('Você realizou {} pontos'.format(pontos), end='\n\n')
            break
        else:
            if maior:
                print('**Você errou! Não fique triste, o seu chute for maior que o número secreto**', end='\n\n')
            elif menor:
                print('**Você errou! Não fique triste, o seu chute for menor que o número secreto**', end='\n\n')

            pontos_perdidos = abs(num_secreto - num_chute)
            pontos = pontos - pontos_perdidos


def voltar_ao_menu():
    voltar = input('Deseja voltar ao menu principal? s/n ')
    print('\n')
    if voltar == 'n':
        print('Feche o console.')
    else:
        menu_jogos.menu_jogos()
        print('\n\n')


if __name__ == '__main__':
    jogar()
