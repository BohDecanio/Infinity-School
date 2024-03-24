
lista_tarefas = []
lista_categorias = ['geral', '1']

#Cria uma nova tarefa
def cria_categorias(nome_categoria):
    lista_categorias.append(nome_categoria)

#faz listagem de tarefas cadastradas
def listar_tarefas():
    print('\n >>> Lista de Tarefas: ')
    for tarefa in lista_tarefas:
        print('')
        print(tarefa)
   
#marca True para o atributo: completada. Indica a tarefa concluida
def marcar_tarefas():
    from Tarefa import Tarefa
    print('Marque a tarefa concluída:')
    listar_tarefas()
    indice_marcar_tarefa = int(input('\n Escolha o índice da tarefa a ser marcada como concluída.\n Sendo a primeira tarefa o índice 0; a segunda, índice 1 e assim sucessivamente...\n'))
    
    if indice_marcar_tarefa >= 0 and indice_marcar_tarefa < len(lista_tarefas):
        lista_tarefas[indice_marcar_tarefa].completada = True
        print('Tarefa marcada como concluída com sucesso!')
    else:
        print('Índice inválido. Por favor, escolha um índice válido.')

    listar_tarefas()

#lista as tarefas por ordem de prioridade
def Listar_Tarefas_prioridade():
    print('\n >>> Lista de Tarefas ordenadas por prioridade: ')
    
    # Primeiro, vamos criar listas separadas para cada prioridade
    tarefas_alta_prioridade = []
    tarefas_media_prioridade = []
    tarefas_baixa_prioridade = []

    # Em seguida, vamos separar as tarefas nas listas correspondentes
    for tarefa in lista_tarefas:
        if tarefa.prioridade == 'alta':
            tarefas_alta_prioridade.append(tarefa)
        elif tarefa.prioridade == 'media':
            tarefas_media_prioridade.append(tarefa)
        elif tarefa.prioridade == 'baixa':
            tarefas_baixa_prioridade.append(tarefa)

    # Por fim, vamos imprimir as tarefas em ordem de prioridade
    for tarefa in tarefas_alta_prioridade:
        print(tarefa)
    for tarefa in tarefas_media_prioridade:
        print(tarefa)
    for tarefa in tarefas_baixa_prioridade:
        print(tarefa)

#lista tarefas por categorias
def Listar_Tarefas_Categoria():
    print('\n >>> Lista de Tarefas por categoria: ')

    # Criar um conjunto para armazenar todas as categorias presentes nas tarefas
    categorias = set(tarefa.categoria for tarefa in lista_tarefas)

    # Para cada categoria, listar as tarefas correspondentes
    for categoria in categorias:
        print(f'\nCategoria: {categoria}')
        for tarefa in lista_tarefas:
            if tarefa.categoria == categoria:
                print(tarefa)

#cria uma nova categoria
def criar_categoria():
    nova_categoria = input("Digite o nome da nova categoria: ")
    if nova_categoria not in lista_categorias:
        lista_categorias.append(nova_categoria)
        print("Categoria criada com sucesso!")
    else:
        print("Categoria já existe!")

#remove uma teraf que seja existente na lista de tarefas
def remover_Tarefa():
    escolhe_Tarefa_remover = input('Digite o nome da tarefa a ser excluída: ')
    for tarefa in lista_tarefas:
        if tarefa.nome_tarefa == escolhe_Tarefa_remover:
            lista_tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            return  # Parar a função após remover a tarefa
    
    print("Tarefa não existe!")

#lista as categorias já cadastradas
def listar_categorias():
    print('\n >>> Lista de Categorias: ')
    for categoria in lista_categorias:
        print('')
        print(categoria)

#Remove uma categoria existente da lista de categorias
def remover_Categoria():
    escolhe_Categoria_remover = input('Digite o nome da categoria a ser excluída: ')
    for categoria in lista_categorias:
        if categoria == escolhe_Categoria_remover:
            lista_categorias.remove(categoria)
            print("Categoria removida com sucesso!")
            return  # Parar a função após remover a categoria
    
    print("Categoria não existe!")