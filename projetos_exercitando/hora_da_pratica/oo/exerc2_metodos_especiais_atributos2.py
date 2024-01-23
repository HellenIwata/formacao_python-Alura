def executar_exercicios():
    pass
#1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
    class Carro:
        def __init__(self, modelo, cor, ano):
            self.modelo = modelo
            self.cor = cor
            self.ano = ano
            
    carro1 = Carro('Sedan', 'Mercurio', 2018)

#2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
    class Restaurante:
        def __init__(self, nome, categoria, capacidade, tempo_atendimento, ativo=False):
            self.nome = nome
            self.categoria = categoria
            self.ano_abertura = capacidade
            self.tempo_atendimento = tempo_atendimento
            self.ativo = ativo
        
    restaurante1 = Restaurante('Boteco do Zé', 'Tradicional', 1950, 30, ativo=True)

#3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
    class Restaurante:
        def __init__(self, nome, categoria, ativo=False):
            self.nome = nome
            self.categoria = categoria
            self.ativo = ativo
        
    restaurante1 = Restaurante('Boteco do Zé', 'Tradicional')

#4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    class Restaurante:
        def __init__(self, nome, categoria, ativo=False):
            self.nome = nome
            self.categoria = categoria
            self.ativo = ativo
            
        def __str__(self):
            return f'{self.nome} | {self.categoria}'
        
#5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
    class Cliente:
        def __init__(self, nome, idade, genero, pontos_acumulados):
            self.nome = nome
            self.idade = idade
            self.genero = genero
            self.pontos_acumulados = pontos_acumulados
            
    cliente1 = Cliente('Heloisa', 30, 'FEM', 800)
    cliente2 = Cliente('Gabriela', 18, 'Fluído', 350)
    cliente3 = Cliente('Antony', 22, "MASC", 1350)
        


if __name__ == '__main__':
    executar_exercicios()