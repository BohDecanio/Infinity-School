import sqlite3
from model import Produto, Venda

class GerenciadorEstoque:
    def __init__(self, db_name):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def adicionar_produto(self, produto):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO estoque (nome_produto, descricao, quantidade, preco_unitario, valor_total)
        VALUES (?, ?, ?, ?, ?)
        ''', (produto.nome_produto, produto.descricao, produto.quantidade, produto.preco_unitario, produto.valor_total))
        conn.commit()
        conn.close()

    def atualizar_quantidade_produto(self, id, quantidade):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE estoque
        SET quantidade = ?, valor_total = quantidade * preco_unitario
        WHERE id = ?
        ''', (quantidade, id))
        conn.commit()
        conn.close()

    def registrar_venda(self, venda):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO vendas (id_produto, quantidade, preco_unitario, valor_total, data_venda)
        VALUES (?, ?, ?, ?, ?)
        ''', (venda.id_produto, venda.quantidade, venda.preco_unitario, venda.valor_total, venda.data_venda))
        cursor.execute('''
        UPDATE estoque
        SET quantidade = ?, valor_total = quantidade * preco_unitario
        WHERE id = ?
        ''', (venda.quantidade, venda.id_produto))
        conn.commit()
        conn.close()

    def gerar_relatorio_estoque(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM estoque')
        estoque = cursor.fetchall()
        conn.close()
        return estoque
