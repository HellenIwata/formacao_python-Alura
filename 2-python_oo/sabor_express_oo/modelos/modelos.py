class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print('Nome | Categoria | Status')
        for restaurante in Restaurante.restaurantes:
            
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
            


restaurante_sushi_iwata = Restaurante('Iwata Sushi', 'Japonês')
#restaurante_sushi_iwata.nome = 'Iwata Sushi'
#restaurante_sushi_iwata.categoria = 'Japones'
restaurante_jorge_boteco = Restaurante('Boteco do Jorge','Brasileira')

Restaurante.listar_restaurantes()