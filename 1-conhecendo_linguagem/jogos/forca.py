#Função built-in (int()/input()/type()) são aquelas que não precisa importar explicitamente,
#pois elas estão disponíveis para o uso automaticamente
import random
import menu_jogos
#As funções foram declaradas no final do arquivo.


def jogar():
    mensagem_abertura_jogo()

    palavra_secreta = escolha_modo_jogo()

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

    jogar_novamente = input('Deseja jogar novamente? s/n ')
    if jogar_novamente == 'n':
        imprime_mesagem_fim_jogo()
        voltar_ao_menu()
    else:
        jogar()




#Declarando as funções:


def mensagem_abertura_jogo():
    print("*************************************")
    print("********** *Jogo de Forca* **********")
    print("*************************************", end="\n\n")


#Carregas arquivos
def escolha_modo_jogo():
    print("********* *Escolha o modo do jogo:* *********")
    print("********************************************", end="\n")
    print('(1) Palavras Mistas | (2) Frutas  | (3) Profissões', end='\n')
    print('(4)      Nomes      | (5) Animais | (6) Objetos')
    print("********************************************", end="\n")

    modo = int(input("Digite a opção desejada: "))
    print(end="\n")

    print('O modo escolhido é: {}'.format(modo), end='\n\n')

    if modo == 1:
        arquivo = open('./palavras_jogo_forca/01_palavras_secretas_aletórias.txt', 'r', encoding="utf8")
        palavra_mista = []
        for linha in arquivo:
            linha = linha.strip()
            palavra_mista.append(linha)

        arquivo.close()
        # definindo a variável da palavra secreta:
        numero = random.randrange(0, len(palavra_mista))
        palavra_secreta = palavra_mista[numero].upper()
        return palavra_secreta

    elif modo == 2:
        arquivo = open('./palavras_jogo_forca/02_frutas_palavras_secretas.txt', 'r', encoding="utf8")
        frutas_palavras = []
        for linha in arquivo:
            linha = linha.strip()
            frutas_palavras.append(linha)

        arquivo.close()
        # definindo a variável da palavra secreta:
        numero = random.randrange(0, len(frutas_palavras))
        palavra_secreta = frutas_palavras[numero].upper()
        return palavra_secreta

    elif modo == 3:
        arquivo = open('./palavras_jogo_forca/03_profissoes_palavras_secretas.txt', 'r', encoding="utf8")
        profissoes_palavras = []
        for linha in arquivo:
            linha = linha.strip()
            profissoes_palavras.append(linha)

        arquivo.close()
        # definindo a variável da palavra secreta:
        numero = random.randrange(0, len(profissoes_palavras))
        palavra_secreta = profissoes_palavras[numero].upper()
        return palavra_secreta

    elif modo == 4:
        arquivo = open('./palavras_jogo_forca/04_nomes_palavras_secretas.txt', 'r', encoding="utf8")
        nomes = []
        for linha in arquivo:
            linha = linha.strip()
            nomes.append(linha)

        arquivo.close()
        # definindo a variável da palavra secreta:
        numero = random.randrange(0, len(nomes))
        palavra_secreta = nomes[numero].upper()
        return palavra_secreta

    elif modo == 5:
        arquivo = open('./palavras_jogo_forca/05_animais_palavras_secretas.txt', 'r', encoding="utf8")
        animais = []
        for linha in arquivo:
            linha = linha.strip()
            animais.append(linha)

        arquivo.close()

        # definindo a variável da palavra secreta:
        numero = random.randrange(0, len(animais))
        palavra_secreta = animais[numero].upper()
        return palavra_secreta

    else:
        arquivo = open('./palavras_jogo_forca/06_objetos_palavras_secretas.txt', 'r', encoding="utf8")
        objetos = []
        for linha in arquivo:
            linha = linha.strip()
            objetos.append(linha)

        arquivo.close()

        # definindo a variável da palavra secreta:
        numero = random.randrange(0, len(objetos))
        palavra_secreta = objetos[numero].upper()
        return palavra_secreta

#def carrega_arquivo_palavra_secreta():
    #arquivo = open('palavras_secretas.txt', 'r', encoding="utf8")
    #frutas = []
    #for linha in arquivo:
    #    linha = linha.strip()
    #    frutas.append(linha


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




def voltar_ao_menu():
    voltar = input('Deseja voltar ao menu principal? s/n ')
    print('\n')
    if voltar == 'n':
        print('Feche o console.')
    else:
        menu_jogos.menu_jogos()
        print('\n\n')



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
            print("A palavra era {}".format(palavra_secreta), end='\n\n')


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
