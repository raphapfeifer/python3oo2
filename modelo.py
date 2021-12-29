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

    def imprime(self):
        print({self._nome} - {self.ano} - {self._likes})

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def imprime(self):
        print({self._nome} - {self.ano} - {self.duracao} - {self._likes})

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print({self._nome} - {self.ano} - {self.temporadas} - {self._likes})


filme = Filme('vingadores - guerra infinita', 2018,160)
filme.dar_like()

serie = Serie('Bad batch', 2021, 1)
serie.dar_like()
serie.dar_like()

filmes_e_series = [filme,serie]

for programa in filmes_e_series:
    programa.imprime()