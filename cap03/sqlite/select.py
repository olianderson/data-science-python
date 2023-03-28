import sqlite3
import random
import time
import datetime
 
# Criando uma conexão
conn = sqlite3.connect('./cap06/arquivos/bancosqlite.db')   

# Criando um cursor
c = conn.cursor()
 
# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)')

# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES(002, '02-05-2020', 'teclado', 130 )")
    conn.commit()
    c.close()
    conn.close()
    
# Usando variáveis para inserir dados    
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_valor:float = random.randrange(20,100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?)", 
              (new_date, new_prod_name, new_valor))
    conn.commit()
    
# Leitura de dados
def leitura_todos_dados():
    c.execute("SELECT * FROM produtos")
    for linha in c.fetchall():
        print(f'Produto: {linha}')
        
# Leitura de registros específicos
def leitura_registros():
    c.execute("SELECT * FROM produtos WHERE valor > 60.0")
    for linha in c.fetchall():
        print(f'Maior que R$ 60.00 {linha}')      
        
# Leitura de colunas específicos
def leitura_colunas():
    c.execute("SELECT * FROM produtos")
    for linha in c.fetchall():
        print(f'Valor: R$ {linha[3]:.2f}')         


# Select nos dados
leitura_todos_dados()
# Leitura de registros específicos
leitura_registros()
# Leitura de colunas específicas
leitura_colunas()

# Encerrando a conexão
c.close()
conn.close()