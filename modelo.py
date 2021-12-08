class Filme:
    def __init__(self,nome,ano,duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self,nome,ano,temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
            self.likes += 1


filme = Filme('vingadores - guerra infinita', 2018,160)
filme.dar_like()

print("O filme se chama {} foi lançado em {} e tem a duração de {} minutos. Teve {} likes".format(filme.nome,filme.ano,filme.duracao,filme.likes))

serie = Serie('Bad batch', 2021, 1)
serie.dar_like()
serie.dar_like()
print("A serie é {} lançada no ano {} e que tem {} temporada(s).Teve {} likes".format(serie.nome,serie.ano,serie.temporadas,serie.likes))