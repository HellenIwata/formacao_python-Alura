from modelos.restaurante import Restaurante

restaurante_sushi_iwata = Restaurante('Iwata Sushi', 'Japonês')
restaurante_jorge_boteco = Restaurante('Boteco do Jorge','Brasileira')
restaurante_muy_loca = Restaurante('Muy Loca', 'Mexicana')

restaurante_muy_loca.alterar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()