# Reemove o arquivo com o banco de dados SQLite (caso exista)
import os
import sqlite3

os.remove("./cap06/arquivos/bancosqlite.db") if os.path.exists("./cap06/arquivos/bancosqlite.db") else None
 
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
    c.execute("INSERT INTO produtos VALUES(1001, '2020-05-02 14:32:11', 'Teclado', 90.00 )")
    conn.commit()
    c.close()
    conn.close()

# Criar tabela
create_table()
# Inserir dados
data_insert()