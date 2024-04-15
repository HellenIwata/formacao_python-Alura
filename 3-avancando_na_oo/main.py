class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._avaliacao = 0
        
    @property
    def avaliacao(self):
        return self._avaliacao
    
    def avaliando(self):
        self._avaliacao += 1
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'
    
class Filme(Programa):
    def __init__(self, nome, diretor, ano, duracao):
        super().__init__(nome, ano)
        self.diretor = diretor
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Diretor: {self.diretor} - Duração: {self.duracao} min - Avaliações: {self._avaliacao}'

class Serie(Programa):
    def __init__(self, nome, diretor, ano, temporada):
        super().__init__(nome, ano)
        self.diretor = diretor
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome} - Diretor: {self.diretor} - Temporadas: {self.temporada} min - Avaliações: {self._avaliacao}'
    
    
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)
    
vingadores = Filme('vingadores - guerra infinita', 'Homem de ferro' ,2018, 160)
atlanta = Serie('atlanta', 'Homem de ferro',2018, 2)
tmep = Filme('todo mundo em panico','Homem de ferro', 1999, 100)
demolidor = Serie('demolidor','Homem de ferro', 2016, 2)

vingadores.avaliando()
vingadores.avaliando()
vingadores.avaliando()

atlanta.avaliando()
atlanta.avaliando()

tmep.avaliando()
tmep.avaliando()

demolidor.avaliando()
demolidor.avaliando()


lista_fnds = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', lista_fnds)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')