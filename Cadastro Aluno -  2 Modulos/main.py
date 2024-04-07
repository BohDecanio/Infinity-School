from funcoes import *

if __name__ == "__main__":
    while True:
        print("\n\n  Menu:")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Alterar nome de Aluno")
        print("4. Ver lista de alunos cadastrados")
        print("5. Sair")

        escolha = input("\n    Escolha uma opção: ")

        if escolha == "1":
            AdicionarAluno()
        elif escolha == "2":
            RemoverAluno()
        elif escolha == "3":
            AtualizarAluno()
        elif escolha == "4":
            VerAlunos()
        elif escolha == "5":
            print("   ## Encerrando o programa... ##")
            break
        else:
            print(" \n *** Opção inválida. Por favor, escolha uma opção válida. De 1 a 5")