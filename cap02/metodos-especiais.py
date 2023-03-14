# Criando a classe Livro
class Livro():
    def __init__(self, titulo, autor, paginas):
        print ("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Retorna o texto            
    def __str__(self):
        return f"Título: {self.titulo}, autor: {self.autor}, páginas: {self.paginas}"

    def __len__(self):
        return self.paginas
    
    def len(self):
        return print("Páginas do livro com método comum: {self.paginas}")

livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816)
# Métodos especiais
print(livro1)
str(livro1)
print(len(livro1))
livro1.len()
# Ao executar a função del para remover um atributo, o Python executa: livro1.__delattr__("paginas")
del livro1.paginas
hasattr(livro1, "paginas")