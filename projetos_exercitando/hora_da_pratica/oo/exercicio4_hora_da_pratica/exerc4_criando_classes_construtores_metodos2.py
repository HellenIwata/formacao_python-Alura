#1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    #2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'

    #3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar_livro(self):
        self._disponivel = not self._disponivel

    #4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano_desejado):
        livros_disponiveis =[livro for livro in Livro.livros if livro._ano_publicacao == ano_desejado and livro._disponivel]
        return livros_disponiveis
        
            

#Criando instância do tópico 3
livro1 = Livro('Percy Jackson e os olimpianos: O cálice dos Deuses', 'Rick Riordan', 2023)
livro1.emprestar_livro()
#print(livro1)

#5.Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

#6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

#7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

#8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.