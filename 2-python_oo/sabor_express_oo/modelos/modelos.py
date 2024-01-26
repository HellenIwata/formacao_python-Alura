class Restaurante:
    restaurantes = []
    
    # Método __init__: é uma função especial que podemos aplicar para iniciar a classe. Ao criar o objeto da classe, o método é aplicado automaticamente e define o comportamento inicial do objeto. 
    # Sintaxe: def __init__(self, *args, **kwargs) onde temos:
        #*args: Utilizado para passar argumentos de construção para a classe, se não houve pode utilizar 'none'
        #**kwargs: Utilizado para passar parâmetros de inicialização para a classe quando fazemos o input de um objeto    
    def __init__(self, nome, categoria):
        self._nome = nome.title() #.title(): Função que retorna obrigatóriamente a primeira letra do texto em maiúscula, funcionamento parecido com o '.upper()'
        self.categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    #Método __str__: é uma função especial utilizado para retornar uma representação de texto
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status\n')
        for restaurante in Restaurante.restaurantes:
            
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
    
    # Decorador @property: utilizado para transformar um método em uma propriedade de uma classe. Ele permite que um método seja acessado como atributo, sem a necessidade de chamá-lo como uma função.
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'            


restaurante_sushi_iwata = Restaurante('Iwata Sushi', 'Japonês')
#restaurante_sushi_iwata.nome = 'Iwata Sushi'
#restaurante_sushi_iwata.categoria = 'Japones'
restaurante_jorge_boteco = Restaurante('Boteco do Jorge','Brasileira')

Restaurante.listar_restaurantes()

