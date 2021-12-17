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


class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao



class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas




filme = Filme('vingadores - guerra infinita', 2018,160)
filme.dar_like()

print("O filme se chama {} foi lançado em {} e tem a duração de {} minutos. Teve {} likes".format(filme.nome,filme.ano,filme.duracao,filme.likes))

serie = Serie('Bad batch', 2021, 1)
serie.dar_like()
serie.dar_like()
print("A serie é {} lançada no ano {} e que tem {} temporada(s).Teve {} likes".format(serie.nome,serie.ano,serie.temporadas,serie.likes))