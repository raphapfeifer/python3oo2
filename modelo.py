class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return self._nome + " " + str(self.ano) + " " + str(self._likes)

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return  self._nome + " " + str(self.ano) + " " + str(self.duracao) + " " + str(self._likes)

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return self._nome + " " + str(self.ano) + " " + str(self.temporadas) + " " + str(self._likes)


class Playlist(list):
    def __init__(self,nome,programas):
        self.nome = nome,
        super().__init__(programas)




vingadores = Filme('vingadores - guerra infinita', 2018,160)
vingadores.dar_like()

tmep = Filme('Todo mundo em pânico', 1999,100)
tmep.dar_like()

bad_batch = Serie('Bad batch', 2021, 1)
bad_batch.dar_like()
bad_batch.dar_like()

demolidor = Serie('Demolidor',2016,2)
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores,bad_batch,tmep]

fim_de_semana = Playlist('fim de semana',filmes_e_series)

print("tamanho do playlist: {}".format(len(fim_de_semana)))

for programa in fim_de_semana:
    print(programa)

print(f'Tá ou não? {demolidor in fim_de_semana}')