#Função built-in (int()/input()/type()) são aquelas que não precisa importar explicitamente,
#pois elas estão disponíveis para o uso automaticamente
import random

#As funções foram declaradas no final do arquivo.


def jogar():
    mensagem_abertura_jogo()
    palavra_secreta = carrega_arquivo_palavra_secreta()

    #Adicionando o caracter '_' para cada letra da palavra secreta
    letras_acertadas = ['_' for letra in palavra_secreta]
    # Exemplo para criar o caracter com a palavra secreta
    # for letra in palavra_secreta:
    #   letras_acertadas.append('_')

    print('A palavra secreta tem {} letra(s).'.format(len(letras_acertadas)), end='\n')
    print(letras_acertadas, end='\n\n')

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_letra()

        if chute in palavra_secreta:
            marca_letra_certa(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        #criando a lógica para finalizar o jogo quando errar ou acertar
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    condicao_ganhar_perder_jogo(acertou, palavra_secreta)

    jogar_novamente = input('Deseja jogar novamente? s/n', end='\n')
    if jogar_novamente == 'n':
        imprime_mesagem_fim_jogo()
    else:
        jogar()


#Declarando as funções:


def mensagem_abertura_jogo():
    print("*************************************")
    print("********** *Jogo de Forca* **********")
    print("*************************************", end="\n\n")


def carrega_arquivo_palavra_secreta():
    arquivo = open('palavras_secretas.txt', 'r', encoding="utf8")
    frutas = []
    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)

    arquivo.close()

    # definindo a variável da palavra secreta:
    numero = random.randrange(0, len(frutas))
    palavra_secreta = frutas[numero].upper()
    return palavra_secreta


def pede_letra():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def marca_letra_certa(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            # print('Encontrei a letra {} na posição {}'.format(letra, index))
        index += 1


def imprime_mesagem_fim_jogo():
    print("*************************************")
    print("*********** *Fim do jogo* ***********")
    print("*************************************")


def condicao_ganhar_perder_jogo(acertou, palavra_secreta):
    if acertou:
        print("Parabéns, você ganhou!")
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
    else:
            print("Puxa, você foi enforcado!")
            print("A palavra era {}".format(palavra_secreta))
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ", end='\n\n')


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |     ('o')  ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ", end='\n\n')


if __name__ == '__main__':
    jogar()
