from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    '''Esta classe representa um restaurante e suas características'''
    
    '''
    Método __init__: é uma função especial que podemos aplicar para iniciar a classe. Ao criar o objeto da classe, o método é aplicado automaticamente e define o comportamento inicial do objeto. 
    Sintaxe: def __init__(self, *args, **kwargs) onde temos:
        *args: Utilizado para passar argumentos de construção para a classe, se não houve pode utilizar 'none'
        **kwargs: Utilizado para passar parâmetros de inicialização para a classe quando fazemos o input de um objeto    
    '''
    def __init__(self, nome, categoria):
        '''Este método inicializa uma instância do Restaurante.
        Parâmetro:
            nome, categoria (str): o nome respresenta o nome do restaurante e a categoria em qual categoria ela se encaixa.
        '''
        #.title(): Função que retorna obrigatóriamente a primeira letra do texto em maiúscula, funcionamento parecido com o '.upper()'
        self._nome = nome.title() 
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    #Método __str__: é uma função especial utilizado para retornar uma representação de texto
    def __str__(self):
        '''Retorna uma representação de str'''
        return f'{self._nome} | {self.categoria}'
    
    @classmethod #@classmethod: utilizado para se referenciar a métodos que pertençam a classe, e não do objeto. 
    def listar_restaurantes(cls):
        '''Retorna a lista com os restaurantes cadastrados'''
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} | Status\n')
        
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
    
    # Decorador @property: utilizado para transformar um método em uma propriedade de uma classe. Ele permite que um método seja acessado como atributo, sem a necessidade de chamá-lo como uma função.
    @property
    def ativo(self):
        '''Retorna o status do restaurante cadastrado'''
        return '☑' if self._ativo else '☐'   
    
    def alterar_status(self):
        '''Altera o status do restaurante cadastrado'''
        self._ativo = not self._ativo

    @property
    def receber_avaliacao(self, cliente, nota):
        '''Recebe as avaliações dos restaurantes cadastros e verifica se a nota esta dentro dos parâmetros para seguir com o calculo da média
            cliente (str) = nome do cliente que digitou a nota
            nota(float) = nota atribuída ao restaurante
        '''
        if 0>=  nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        '''Se houver avaliações vinculadas com o restaurante cadastrado, esta função irá calcular e retornar a média das avaliações do restaurante'''
        if not self._avaliacao:
            return 'Este restaurante não tem nenhuma avaliação'
        somar_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_avaliacoes = len(self._avaliacao)
        media_avaliacoes = round(somar_avaliacoes / quantidade_avaliacoes, 1)
        return media_avaliacoes

    def adicionar_ao_cardapio(self, item):
        """Se houver item ele será adicionado ao cardápio, esta função irá verificar se o item passado é uma instância da classe itemCardapio ou classe derivada dela """
        if isinstance(item, ItemCardapio): #Função isinstance: Será verdadeira se o item que é passado como argumento for uma instância da classe itemCardapio ou se for uma classe derivada de itemCardapio
            self._cardapio.append(item)
    
                
    