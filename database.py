import sqlite3

class Database:
    def __init__(self):
        self.db_name = "sistema_academico.db"
        self.conexao = sqlite3.connect(self.db_name)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS alunos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                idade INTEGER,
                                cep TEXT,
                                email TEXT,
                                cpf TEXT
                            )
                        ''')

            # Criação da tabela cursos
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS cursos (
                    curso_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL
                )
            ''')

            # Criação da tabela turmas
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS turmas (
                    turma_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    curso_id INTEGER,
                    turno TEXT NOT NULL,
                    FOREIGN KEY(curso_id) REFERENCES cursos(curso_id)
                )
            ''')

            # Criação da tabela turmas
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS alunos_turmas (
                                aluno_id INTEGER,
                                turma_id INTEGER,
                                PRIMARY KEY (aluno_id, turma_id),
                                FOREIGN KEY (aluno_id) REFERENCES alunos(id),
                                FOREIGN KEY (turma_id) REFERENCES turmas(turma_id)
                            )
                        ''')


            self.conexao.commit()
            print("Tabelas 'cursos' e 'turmas' criadas ou já existentes.")
        except Exception as e:
            print(f"Erro ao criar as tabelas: {e}")

    def execute(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conexao.commit()
        except Exception as e:
            print(f"Erro ao executar a query: {e}")

    def close(self):
        self.conexao.close()
