from veiculo import Veiculo
#5. Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self._esportiva = False
        
    #6. Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    def __str__(self) -> str:
        return f'{self._marca} | {self._modelo} | {self._esportiva}'
    
#7. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
#8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
#9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.