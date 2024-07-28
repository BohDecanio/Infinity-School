import sqlite3
from sqlite3 import Error

def create_database(db_name):
    print(f"Criando DB SQLite: {db_name}")

    conn = None

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

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

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto INTEGER,
            quantidade INTEGER NOT NULL,
            preco_unitario REAL NOT NULL,
            valor_total REAL NOT NULL,
            data_venda TEXT NOT NULL,
            FOREIGN KEY (id_produto) REFERENCES produtos (id)
        )
        ''')

        conn.commit()
        print("Banco de dados e tabelas criados com sucesso")
    except Error as e:
        print(f"Erro: {e}")
    finally:
        if conn:
            conn.close()
