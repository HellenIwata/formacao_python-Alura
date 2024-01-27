from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    '''
    Método __init__: é uma função especial que podemos aplicar para iniciar a classe. Ao criar o objeto da classe, o método é aplicado automaticamente e define o comportamento inicial do objeto. 
    Sintaxe: def __init__(self, *args, **kwargs) onde temos:
        *args: Utilizado para passar argumentos de construção para a classe, se não houve pode utilizar 'none'
        **kwargs: Utilizado para passar parâmetros de inicialização para a classe quando fazemos o input de um objeto    
    '''
    def __init__(self, nome, categoria):
        #.title(): Função que retorna obrigatóriamente a primeira letra do texto em maiúscula, funcionamento parecido com o '.upper()'
        self._nome = nome.title() 
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    #Método __str__: é uma função especial utilizado para retornar uma representação de texto
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod #@classmethod: utilizado para se referenciar a métodos que pertençam a classe, e não do objeto. 
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} | Status\n')
        
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
    
    # Decorador @property: utilizado para transformar um método em uma propriedade de uma classe. Ele permite que um método seja acessado como atributo, sem a necessidade de chamá-lo como uma função.
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'   
    
    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        somar_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_avaliacoes = len(self._avaliacao)
        media_avaliacoes = round(somar_avaliacoes / quantidade_avaliacoes, 1)
        return media_avaliacoes

