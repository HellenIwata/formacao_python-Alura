#end="\n" -> Pular linha
import forca
import adivinhacao

def escolha_jogos():
    print("*************************************")
    print("***** *Escolha o jogo desejado* *****")
    print("*************************************", end="\n\n")

    print('(1) Forca (2) Adivinhação')
    jogo = int(input("Escolha o número do jogo: "))

    if(jogo == 1):
        print('Iniciando o jogo de Forca')
        forca.jogar()
    elif(jogo == 2):
        print('Iniciando o jogo de Adivinhação')
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolha_jogos()