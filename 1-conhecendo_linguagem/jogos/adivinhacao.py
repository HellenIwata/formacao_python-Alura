# biblioteca importada para sortear os números aleatórios do jogo
import random


def jogar():
    print("*************************************")
    print("******* *Jogo de Adivinhação* *******")
    print("*************************************", end="\n\n")

    num_secreto = random.randrange(1,
                                   101)  # Definindo quais números podem ser escolhidos para ser o secreto (entre 1 e 100)
    total_de_tentativas = 0
    pontos = 1000

    # Criando o nível de dificuldade do jogo
    print("********* *Escolha a dificuldade:* *********")
    print("********************************************", end="\n")
    print('(1) Fácil | (2) Intermediário | (3) Difícil')
    print("********************************************", end="\n")

    nivel = int(input("Digite a opção desejada: "))
    print(end="\n\n")

    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Iniciando a sequencia do jogo
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
            print('**Parabéns! Você acertou**', end='\n')
            print('Você realizou {} pontos'.format(pontos), end='\n\n')
            break
        else:
            if maior:
                print('**Você errou! Não fique triste, o seu chute for maior que o número secreto**', end='\n\n')
            elif menor:
                print('**Você errou! Não fique triste, o seu chute for menor que o número secreto**', end='\n\n')

            pontos_perdidos = abs(num_secreto - num_chute)
            pontos = pontos - pontos_perdidos

    print("*************************************")
    print("*********** *Fim do jogo* ***********")
    print("*************************************")


if __name__ == '__main__':
    jogar()
