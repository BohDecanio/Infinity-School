class MaterialView:
    def exibir_informacoes(self, material):
        material.exibir_informacoes()

    def obter_acao(self):
        print("\n\n   Escolha uma ação: \n")
        print("1: Adicionar Livro")
        print("2: Adicionar Revista")
        print("3: Exibir informações de Livros")
        print("4: Exibir informações de Revistas")
        print("5: Sair")
        return input("\n Ação: \n ")

    def obter_dados_livro(self):
        titulo = input("Título do Livro: ")
        autor = input("Autor do Livro: ")
        genero = input("Gênero do Livro: ")
        return titulo, autor, genero

    def obter_dados_revista(self):
        titulo = input("Título da Revista: ")
        editora = input("Editora da Revista: ")
        edicao = input("Edição da Revista: ")
        return titulo, editora, edicao

    def exibir_mensagem(self, mensagem):
        print(mensagem)
