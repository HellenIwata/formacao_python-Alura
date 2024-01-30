class Avaliacao:
    '''Esta classe representa uma avaliação e suas características'''
    def __init__(self, cliente, nota):
        '''Este método inicializa uma instância da avaliação.
        Parâmetro:
            cliente (str): respresenta o nome do cliente que iniciou a avaliação
            nota (float): nota atribuída ao restaurante
        '''
        self._cliente = cliente
        self._nota = nota
    