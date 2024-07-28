from model import Produto, Venda, GerenciadorEstoque

def menu_vendas():
    gerenciador = GerenciadorEstoque()

    while True:
        print("\n\n       Sistema de gerenciamento de vendas: \n\n")
        print("1. Adicionar produto")
        print("2. Atualizar quantidade de produto")
        print("3. Registrar venda")
        print("4. Relatório de vendas")
        print("5. Listar produtos cadastrados")
        print("6. Excluir produto")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            descricao = input("Descrição do produto: ")
            quantidade = int(input("Quantidade: "))
            preco_unitario = float(input("Preço unitário: "))
            produto = Produto(nome, descricao, quantidade, preco_unitario)
            gerenciador.adicionar_produto(produto)
            print("Produto adicionado com sucesso!")

        elif opcao == "2":
            id_produto = int(input("ID do produto a ser atualizado: "))
            nova_quantidade = int(input("Nova quantidade: "))
            gerenciador.atualizar_estoque(id_produto, nova_quantidade)
            print("Quantidade atualizada com sucesso!")

        elif opcao == "3":
            id_produto = int(input("ID do produto vendido: "))
            quantidade = int(input("Quantidade vendida: "))
            preco_unitario = float(input("Preço unitário: "))
            venda = Venda(id_produto, quantidade, preco_unitario)
            gerenciador.registrar_venda(venda)
            print("Venda registrada com sucesso!")

        elif opcao == "4":
            vendas = gerenciador.relatorio_vendas()
            for venda in vendas:
                print(venda)

        elif opcao == "5":
            produtos = gerenciador.listar_produtos()
            for produto in produtos:
                print(produto)

        elif opcao == "6":
            id_produto = int(input("ID do produto a ser excluído: "))
            gerenciador.excluir_produto(id_produto)
            print("Produto excluído com sucesso!")

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")
