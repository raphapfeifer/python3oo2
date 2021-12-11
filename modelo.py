class Filme:
    def __init__(self,nome,ano,duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

class Serie:
    def __init__(self,nome,ano,temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
            self.__likes += 1


filme = Filme('vingadores - guerra infinita', 2018,160)
filme.dar_like()

print("O filme se chama {} foi lançado em {} e tem a duração de {} minutos. Teve {} likes".format(filme.nome,filme.ano,filme.duracao,filme.likes))

serie = Serie('Bad batch', 2021, 1)
serie.dar_like()
serie.dar_like()
print("A serie é {} lançada no ano {} e que tem {} temporada(s).Teve {} likes".format(serie.nome,serie.ano,serie.temporadas,serie.likes))