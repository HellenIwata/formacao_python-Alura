from cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
    
    def __str__(self) -> str:
        return f'{self._nome} | {self._preco} | {self._tipo} | {self._tamanho}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)
        