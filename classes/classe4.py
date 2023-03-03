class Livro:
    def __init__(self, titulo, autor, editora, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
        self.disponivel = True
        self.emprestado_por = None

    def emprestar(self, nome):
        if self.disponivel:
            self.disponivel = False
            self.emprestado_por = nome
            print("Livro emprestado com sucesso!")
        else:
            print("Este livro não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            self.emprestado_por = None
            print("Livro devolvido com sucesso!")
        else:
            print("Este livro já está disponível para empréstimo.")

    def esta_disponivel(self):
        return self.disponivel


livro1 = Livro("O Hobbit", "J.R.R. Tolkien", "HarperCollins", 310)


print(livro1.titulo)
print(livro1.autor)
print(livro1.editora)
print(livro1.paginas)
print(livro1.esta_disponivel())

livro1.emprestar("Ana")
print(livro1.esta_disponivel())

livro1.devolver()
print(livro1.esta_disponivel())

livro1.devolver()
print(livro1.esta_disponivel())
