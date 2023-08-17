
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.likes} likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self.likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temps - {self.likes} likes"

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

# faz Playlist s ecomportar como lista
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
tmep = Filme("todo mundo em panico", 1999, 100)

atlanta = Serie("Atlanta", 2018, 2)
demolidor = Serie("demolidor", 2016, 2)

demolidor.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(playlist_fim_de_semana[1])

print(demolidor in playlist_fim_de_semana)