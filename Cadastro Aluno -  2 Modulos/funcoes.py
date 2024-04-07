alunos = {}  

def AdicionarAluno():
    if len(alunos) == 0:
        print('\n   Será a primeira matrícula. Insira o valor: 1 e dê sequencia a ordem crescente.')
    print(f'O tamanho da lista alunos é: ',len(alunos))
    
    matricula = int(input("\n       Digite a próxima matrícula de aluno: "))
    nome = input("       Digite o nome do aluno: ")
    alunos[matricula] = nome
    print("\n               Aluno adicionado com sucesso!")

def RemoverAluno():
    matricula = input("\n       Digite a matrícula do aluno para remover: ")
    matricula = int(matricula)
    if matricula in alunos:
        del alunos[matricula]
        print("              Aluno removido com sucesso!")
    else:
        print("              Aluno não encontrado.")

def AtualizarAluno():
    matricula = input("\n       Digite a matrícula do aluno para atualizar: ")
    matricula = int(matricula)
    if matricula in alunos:
        novo_nome = input("           Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print("              Nome do aluno atualizado com sucesso!")
    else:
        print("       Aluno não encontrado.")

def VerAlunos():
    if alunos:
        print("\n       Lista de Alunos:")
        for matricula, nome in alunos.items():
            print("       Matrícula: ", matricula, "- Nome: ", nome)
    else:
        print("       Nenhum aluno cadastrado.")