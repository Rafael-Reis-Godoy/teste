class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
pessoa1 = Pessoa("Ana", 25, "Feminino")
pessoa2 = Pessoa("Rafael", 37, "Masc")

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.sexo)

print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa2.sexo)

