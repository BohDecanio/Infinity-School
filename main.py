from view import menu_vendas
from controller import create_database

if __name__ == "__main__":
    create_database('db_estoque.db')
    menu_vendas()
