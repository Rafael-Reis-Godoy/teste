import datetime

class Funcionario:
    def __init__(self, nome, cargo, salario, data_admissao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao

    def calcular_tempo_servico(self):
        hoje = datetime.date.today()
        tempo_servico = hoje.year - self.data_admissao.year
        if hoje.month < self.data_admissao.month or (hoje.month == self.data_admissao.month and hoje.day < self.data_admissao.day):
            tempo_servico -= 1
        return tempo_servico

funcionario1 = Funcionario("João", "Gerente de Vendas", 5000, datetime.date(2018, 1, 1))
funcionario2 = Funcionario("Maria", "Assistente Administrativo", 2500, datetime.date(2019, 6, 1))


print(funcionario1.nome)
print(funcionario1.cargo)
print(funcionario1.salario)
print(funcionario1.data_admissao)
print(funcionario1.calcular_tempo_servico())

print(funcionario2.nome)
print(funcionario2.cargo)
print(funcionario2.salario)
print(funcionario2.data_admissao)
print(funcionario2.calcular_tempo_servico())
