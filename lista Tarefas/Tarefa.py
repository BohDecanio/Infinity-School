
class Tarefa:
    def __init__(self, nome_tarefa, prioridade, categoria, descricao, completada=False): 
        self.nome_tarefa = nome_tarefa
        self.prioridade = prioridade
        self.categoria = categoria
        self.descricao = descricao
        self.completada = completada

    def __str__(self):
        return f"Nome: {self.nome_tarefa}, Prioridade: {self.prioridade}, Categoria: {self.categoria}, Descrição: {self.descricao}, Completada: {self.completada}"
       
       