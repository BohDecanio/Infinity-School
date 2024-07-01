from model import Livro, Revista

class MaterialController:
    def __init__(self, view):
        self.view = view
        self.materiais = []

    def adicionar_material(self, material):
        self.materiais.append(material)

    def executar(self):
        while True:
            acao = self.view.obter_acao()
            if acao == "1":
                titulo, autor, genero = self.view.obter_dados_livro()
                livro = Livro(titulo, autor, genero)
                self.adicionar_material(livro)
                self.view.exibir_mensagem(" \n   Livro adicionado com sucesso! \n")
            elif acao == "2":
                titulo, editora, edicao = self.view.obter_dados_revista()
                revista = Revista(titulo, editora, edicao)
                self.adicionar_material(revista)
                self.view.exibir_mensagem("\n    Revista adicionada com sucesso! \n")
            elif acao == "3":
                for indice, material in enumerate(self.materiais):
                    if isinstance(material, Livro):
                        self.view.exibir_informacoes(material)
                        print("\n")
            elif acao == "4":
                for indice, material in enumerate(self.materiais):
                    if isinstance(material, Revista):
                        self.view.exibir_informacoes(material)
                        print("\n")
            elif acao == "5":
                print("\n   Saindo do programa... \n")
                break
            else:
                print("\n   ## Ação inválida! Tente novamente... ##\n")
