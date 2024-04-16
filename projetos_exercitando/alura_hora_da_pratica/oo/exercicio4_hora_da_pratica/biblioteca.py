#5.Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from exerc4_criando_classes_construtores_metodos2 import Livro
#6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro2 = Livro('O último dos magos', 'Lisa Maxwell', 2017)

print(f'Validação antes do empréstimo do livro, o Livro esta disponível? {livro2._disponivel}')
livro2.emprestar_livro()
print(f'Validação após o empréstimo do livro, o Livro esta disponível? {livro2._disponivel}')

#7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_desejado = 2018
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_desejado)
print(f"Livros disponíveis em {ano_desejado}: {livros_disponiveis_ano}")

#8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.