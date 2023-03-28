
# Reemove o arquivo com o banco de dados SQLite (caso exista)
import os
os.remove('./cap03/arquivos/escola.db') if os.path.exists('./cap03/arquivos/escola.db') else None

# Importando o módulo de acesso ao SQLite
import sqlite3

# Cria uma conexão com o banco de dados. Se o banco de dados não existir, ele é criado neste momento.
con = sqlite3.connect('./cap03/arquivos/escola.db')

# Criando um cursor (Um cursor permite percorrer todos os registros em um conjunto de dados)
cur = con.cursor()

# Criando comando sql para criação de tabela
sql_create_table = 'CREATE TABLE cursos '\
'(id INTEGER PRIMARY KEY, '\
'titulo VARCHAR(100), '\
'categoria VARCHAR(140))'

# Executando a instrução sql para criar a tabela no banco
cur.execute(sql_create_table)

# Criando outra sentença SQL para inserir registros
sql_insert = 'INSERT INTO cursos VALUES(?, ?, ?)'

# Inserindo registros iniciais
recset = [(1001, 'Ciência de Dados', 'Data Science'),
          (1002, 'Big Data Fundamentos', 'Big Data'),
          (1003, 'Python Fundamentos', 'Análise de Dados')]

# Inserindo os registros para cada registo já inserido
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a transação
con.commit()

# Criando outra sentença SQL para selecionar registros
sql_select = 'SELECT * FROM cursos'

# Seleciona todos os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()

# Mostra
for linha in dados:
    print ('Curso Id: %d, Título: %s, Categoria: %s \n' % linha)

# Gerando outros registros
recset = [(1004, 'Gestão de Dados com MongoDB', 'Big Data'),
          (1005, 'R Fundamentos', 'Análise de Dados')]

# Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)
    
# Gravando a transação
con.commit()

# Seleciona todos os registros
cur.execute('SELECT * FROM cursos')

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print ('Curso Id: %d, Título: %s, Categoria: %s \n' % rec)

# Fecha a conexão
con.close()