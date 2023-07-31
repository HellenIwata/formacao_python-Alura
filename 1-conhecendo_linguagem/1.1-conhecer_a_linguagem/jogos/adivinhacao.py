import random #importando biblioteca para sortear os números aleatório do jogo
#end="\n" -> Pular linha

def jogar():
    print("*************************************")
    print("******* *Jogo de Adivinhação* *******")
    print("*************************************", end="\n\n")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    #Definindo o nível de dificuldade do Jogo
    print("Escolha o nível de dificuldade:")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    nível = int(input("Digite o número do nível (1, 2 ou 3): "))
    print(end="\n\n")

    if (nível == 1):
        total_de_tentativas = 15
    elif(nível == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos), end="\n\n")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.", end="\n\n")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.", end="\n\n")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("*************************************")
    print("*********** *Fim do jogo* ***********")
    print("*************************************")

if(__name__ == '__main__'):
    jogar()