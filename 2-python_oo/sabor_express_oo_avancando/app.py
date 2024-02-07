from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_sushi_iwata = Restaurante('Iwata Sushi', 'Japonês')
bebida_suco = Bebida('Coca-Cola', 8.00, 'M')
prato_yakissoba = Prato('Yakissoba tradicional', 45.50, 'Yakissoba tradicional com carne, frango e legumes')

# restaurante_jorge_boteco = Restaurante('Boteco do Jorge','Brasileira')
# restaurante_muy_loca = Restaurante('Muy Loca', 'Mexicana')


def main():
    restaurante_sushi_iwata.adicionar_ao_cardapio(prato_yakissoba)
    restaurante_sushi_iwata.adicionar_ao_cardapio(bebida_suco)
    
    restaurante_sushi_iwata.listar_cardapio

if __name__ == '__main__':
    main()