from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #Indica que a classe Prato herda métodos e atributos da classe ItemCardapio (Herança)
    
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco) #Super(): é um objeto especial que permite o acesso a informações de outra classe
        self._descricao = descricao
        
    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._descricao}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)