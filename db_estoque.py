import sqlite3

def create_database():
    conn = sqlite3.connect('db_estoque.db')
    cursor = conn.cursor()

    # Criação da tabela de produtos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        valor_total REAL NOT NULL
    )
    ''')

    # Criação da tabela de vendas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        valor_total REAL NOT NULL,
        data_venda TEXT NOT NULL,
        FOREIGN KEY(id_produto) REFERENCES produtos(id)
    )
    ''')

    conn.commit()
    conn.close()

create_database()
