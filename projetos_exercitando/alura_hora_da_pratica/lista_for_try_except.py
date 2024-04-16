def executar_exercicios():
    #1-Crie uma lista para cada informação a seguir: Lista de números de 1 a 10; Lista com quatro nomes; Lista com o ano que você nasceu e o ano atual.
    print('''
        Lista de Informações
        ''')

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nomes = ['Anna Clara', 'Alana', 'Dhara', 'Celina']
    anos = [2000, 2024]

    #2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
    print('''
        Percorrendo todos os elementos de uma lista
        ''')

    for  nome in nomes:
        print(f'{nome}')
        print(' ')


    #3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
    print('''
        Soma dos números ímpares de 1 a 10
        ''')
    soma_dos_impares = 0
    for i in range(1, 11, 2):
        soma_dos_impares += i
        print(soma_dos_impares)
        print(' ')

    #4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
    print('''
        Números de 1 a 10 em ordem decrescente
        ''')
    for decrescente in range(10, 0, -1):
        print(decrescente)

    #5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
    print('''
        Tabuda
        ''')

    numero_tabuda = int(input('Digite um número: '))

    for i in range(1, 11):
        tabuda = numero_tabuda * i
        print(tabuda)

    #6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
    print('''
        Soma dos numeros da lista
        ''')
    soma = 0
    try:
        for numero in numeros:
            soma += numero
        print(soma)
    except Exception as e:
        print(f"Algo deu errado: {e}")

    #7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
    print('''
        Media dos valores da lista
        ''')
    soma_valores = 0

    try:
        for valor in numeros:
            soma_valores += valor
        media = soma_valores / len(numeros)
        print(media)
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == '__main__':
    executar_exercicios()