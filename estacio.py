import sqlite3 as conector

def conectar_banco():
    """Inicia a conexão com o banco de dados e retorna o cursor e a conexão."""
    conexao = conector.connect('cadastro.db')
    cursor = conexao.cursor()
    return cursor, conexao

def criar_tabela():
    """Cria as tabelas no banco de dados se não existirem."""
    cursor, conexao = conectar_banco()

    # Criação da tabela Cursos
    sql = ('CREATE TABLE IF NOT EXISTS Cursos ('
           'id_cur INTEGER PRIMARY KEY AUTOINCREMENT,'
           'nome_curso TEXT NOT NULL'
           ')')
    cursor.execute(sql)

    # Criação da tabela Turmas
    sql = ('CREATE TABLE IF NOT EXISTS Turmas ('
           'id_tur INTEGER PRIMARY KEY AUTOINCREMENT,'
           'nome_turma TEXT NOT NULL,'
           'curso_id INTEGER NOT NULL,'
           'FOREIGN KEY (curso_id) REFERENCES Cursos(id_cur))')
    cursor.execute(sql)

    # Criação da tabela Alunos
    sql = ('CREATE TABLE IF NOT EXISTS Alunos ('
           'matricula INTEGER PRIMARY KEY AUTOINCREMENT,'
           'nome TEXT NOT NULL,'
           'idade INTEGER NOT NULL,'
           'cep TEXT NOT NULL,'
           'email TEXT NOT NULL,'
           'cpf TEXT NOT NULL UNIQUE)')
    cursor.execute(sql)

    conexao.commit()  # Chama commit após a criação das tabelas
    cursor.close()    # Fecha o cursor
    conexao.close()   # Fecha a conexão

    print('Tabelas criadas com sucesso!')

def cadastrar_aluno():
    """Cadastra um novo aluno no banco de dados."""
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    cep = input('Digite o CEP do aluno: ')
    email = input('Digite o email do aluno: ')
    cpf = input('Digite o CPF do aluno: ')

    cursor, conexao = conectar_banco()  # Obtém cursor e conexão

    # Insere os dados do aluno
    cursor.execute('''
    INSERT INTO Alunos (nome, idade, cep, email, cpf)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, idade, cep, email, cpf))

    conexao.commit()  # Chama commit após a inserção
    print(f'Aluno {nome} cadastrado com sucesso!')

    cursor.close()    # Fecha o cursor
    conexao.close()   # Fecha a conexão

# Chama a função para criar tabelas e cadastrar um aluno
criar_tabela()
cadastrar_aluno()
