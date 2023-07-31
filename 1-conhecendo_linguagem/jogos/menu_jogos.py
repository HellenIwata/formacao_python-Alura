#end="\n" -> pular linha

import adivinhacao
import forca

def menu_jogos():
    print("*************************************")
    print("***** *Escolha o jogo desejado* *****")
    print("*************************************", end="\n\n")


    print("***** *Menu de jogos* *****")
    print("*************************************", end="\n\n")
    print('(1) Adivinhação || (2) Forca')
    print("*************************************", end="\n\n")
    jogo = int(input('Digite o número do jogo: '))

    if(jogo == 1):
        print('Iniciando o jogo de Adivinhação')
        adivinhacao.jogar()
    elif(jogo == 2):
        print('Iniciando o jogo de Forca')
        forca.jogar()

#Garantido que o arquivo poderá ser executado sozinho (além de outros arquivos)
if(__name__ == '__main__'):
    menu_jogos()