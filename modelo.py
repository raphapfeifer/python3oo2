class Filme:
    def __init__(self,nome,ano,duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self,nome,ano,temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme('vingadores', 2018,160)
print(vingadores.nome)

bad_batch = Serie('Bad Batch', 2021, 1)
print("A serie é {} lançada no ano {} e que tem {} temporada(s) ".format(bad_batch.nome,bad_batch.ano,bad_batch.temporadas))