from Tarefa import Tarefa
from funcoes import *


completada = False
print('''\n\n                   
      __________________________
          Programa de Tarefas      \n ''')

while True: #mantem o programa aberto até ser escolhido opção '0', para encerrar.
    escolha_menu = input('''\n  
                         ___________________________________
                           Escolha a funcao a ser utlizada:
                     
                     1- adicionar tarefa: 
                     2- listar tarefas: 
                     3- marcar tarefa como concluidas: 
                     4- exibir tarefas por ordem de prioridades:
                     5- exibir tarefas por categoria: 
                     6- remover tarefa: 
                     7- criar categoria:
                     8- listar categorias: 
                     9- remover categoria:


                      
                     0- sair do programa:                      
                     
                    ''')

    if escolha_menu == '0':
        break

    elif escolha_menu == '1': #usuario adiciona nova tarefa 
        #add nome_tarefas, prioridade, categoria, descricao, completada(n add , pois inicia false - não completada)
        nome_tarefa = input('Digite o nome da tarefa: ')
        while True:
            prioridade = input('Informe se a prioridade é [B]Baixa, [M]Media ou [A]Alta: ').lower()
            match prioridade:
                case 'b':
                    prioridade = 'baixa'
                    break
                case 'm':
                    prioridade = 'media'
                    break
                case 'a':
                    prioridade = 'alta'
                    break
                case _:
                    print('Opção inválida')
                    continue
        
        print(f'\n >>>Lista de categorias: {lista_categorias} \n')
        while True:
            categoria = input('Informe a categoria da tarefa: ')
            if categoria not in lista_categorias:
                print('Categoria inesxistente...')
                continue
            break

        descricao = input('Digite uma descricao para a tarefa: \n')
        
        lista_tarefas.append(Tarefa(nome_tarefa, prioridade, categoria, descricao, completada=False))
        
        listar_tarefas()

    elif escolha_menu == '2': #lista tarefas já cadastradas 
        listar_tarefas()


    elif escolha_menu == '3': #marcar terafas como concluidas 
        marcar_tarefas()

    elif escolha_menu == '4': #exibir tarefas por ordem de prioridades
        Listar_Tarefas_prioridade()   

    elif escolha_menu == '5': #exibir tarefas por ordem de categoria
        Listar_Tarefas_Categoria() 

    elif escolha_menu == '6': #Remover tarefa
        remover_Tarefa()

    elif escolha_menu == '7': #Criar categoria
        criar_categoria()

    elif escolha_menu == '8': #Listar Categorias
        listar_categorias()

    elif escolha_menu == '9': #Remover Categoria
        remover_Categoria() 

    else:
        print('Opcao invalida. Fechando o programa!\n ')
        break 

