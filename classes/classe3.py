class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.moedas = 0

    def adicionar_pontos(self, pontos):
        self.pontos += pontos

    def adicionar_moedas(self, moedas):
        self.moedas += moedas

    def verificar_vitoria(self):
        if self.moedas >= 10 and self.pontos >= 100:
            return True
        else:
            return False
jogador1 = Jogador("Ana")

print(jogador1.nome)
print(jogador1.pontos)
print(jogador1.moedas)
print(jogador1.verificar_vitoria())

jogador1.adicionar_pontos(50)
jogador1.adicionar_moedas(500)

print(jogador1.pontos)
print(jogador1.moedas)
print(jogador1.verificar_vitoria())

jogador1.adicionar_pontos(5)
jogador1.adicionar_moedas(5)

print(jogador1.pontos)
print(jogador1.moedas)
print(jogador1.verificar_vitoria())
