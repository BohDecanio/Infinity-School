import sqlite3
from datetime import datetime

class Produto:
    def __init__(self, nome, descricao, quantidade, preco_unitario):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.valor_total = quantidade * preco_unitario

class Venda:
    def __init__(self, id_produto, quantidade, preco_unitario):
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.valor_total = quantidade * preco_unitario
        self.data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class GerenciadorEstoque:
    def __init__(self, db_name='db_estoque.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def adicionar_produto(self, produto):
        self.cursor.execute('''
        INSERT INTO produtos (nome, descricao, quantidade, preco_unitario, valor_total)
        VALUES (?, ?, ?, ?, ?)
        ''', (produto.nome, produto.descricao, produto.quantidade, produto.preco_unitario, produto.valor_total))
        self.conn.commit()

    def atualizar_estoque(self, id_produto, nova_quantidade):
        # Obter o preço unitário do produto
        self.cursor.execute('''
        SELECT preco_unitario FROM produtos WHERE id = ?
        ''', (id_produto,))
        preco_unitario = self.cursor.fetchone()[0]
        
        # Atualizar a quantidade e o valor total do produto
        valor_total = nova_quantidade * preco_unitario
        self.cursor.execute('''
        UPDATE produtos
        SET quantidade = ?, valor_total = ?
        WHERE id = ?
        ''', (nova_quantidade, valor_total, id_produto))
        self.conn.commit()

    def registrar_venda(self, venda):
        self.cursor.execute('''
        INSERT INTO vendas (id_produto, quantidade, preco_unitario, valor_total, data_venda)
        VALUES (?, ?, ?, ?, ?)
        ''', (venda.id_produto, venda.quantidade, venda.preco_unitario, venda.valor_total, venda.data_venda))
        self.conn.commit()
        
        # Atualizar quantidade e valor total de produto no estoque
        self.cursor.execute('''
        SELECT quantidade FROM produtos WHERE id = ?
        ''', (venda.id_produto,))
        quantidade_atual = self.cursor.fetchone()[0]

        nova_quantidade = quantidade_atual - venda.quantidade
        novo_valor_total = nova_quantidade * venda.preco_unitario

        self.cursor.execute('''
        UPDATE produtos
        SET quantidade = ?, valor_total = ?
        WHERE id = ?
        ''', (nova_quantidade, novo_valor_total, venda.id_produto))
        self.conn.commit()

    def relatorio_vendas(self):
        self.cursor.execute('''
        SELECT * FROM vendas
        ''')
        return self.cursor.fetchall()

    def listar_produtos(self):
        self.cursor.execute('''
        SELECT * FROM produtos
        ''')
        return self.cursor.fetchall()

    def excluir_produto(self, id_produto):
        self.cursor.execute('''
        DELETE FROM produtos WHERE id = ?
        ''', (id_produto,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
