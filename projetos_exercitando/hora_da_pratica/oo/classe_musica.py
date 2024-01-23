class Musica:
    musicas = []
    def __init__(self, nome, artista_ou_banda, estilo_musical):
        self.nome = nome
        self.artista_ou_banda = artista_ou_banda
        self.estilo_musical = estilo_musical
        Musica.musicas.append(self)
        
    def listar_musicas():
        print('Nome da Musica | Nome do cantor/banda | Estilo musical\n')
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista_ou_banda} | {musica.estilo_musical}\n')

musica1 = Musica('Os meninos estão com os pacotes', 'MC PH', 'Funk')
musica2 = Musica('Lose your self', 'Eminem', 'Rap')
musica3 = Musica('Ta Rocheda', 'Barões da Pisadinha', 'Piseiro')

Musica.listar_musicas()