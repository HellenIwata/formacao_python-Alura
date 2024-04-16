def executar_exercicios():
    #1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
    info_pessoa = {
        'nome':'Hellen', 
        'idade': 23, 
        'cidade':'SP',
        'estado civil':'solteira'
    }

    #2 - Utilizando o dicionário criado no item 1: Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa); Adicione um campo de profissão para essa pessoa; Remova um item do dicionário.
    info_pessoa['nome'] = 'Hellen Cristina'
    info_pessoa['profissão'] = 'Analista de TI'
    del info_pessoa['cidade']
        
    #3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
    numeros = {x: x**2 
        for x in range(1, 6)
    }
    print(numeros)

    #4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
    
    carro = {'marca': 'Toyota', 'modelo': 'Etios', 'ano': 2020, 'preco': 30000.00}
    if 'marca' and 'preco' in carro:
        print("A chave 'marca' e 'preco' existe no dicionário.")
    else:
        print('Chave não localizada')

    #5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
    frase = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..'
    conte_frequencia = {}
    palavras = frase.split()
    for palavra in palavras:
        conte_frequencia[palavra] = conte_frequencia.get(palavra, 0) + 1
    
    print(conte_frequencia)

if __name__ == '__main__':
    executar_exercicios()