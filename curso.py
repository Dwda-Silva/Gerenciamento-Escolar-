import sqlite3

class Curso:
    def __init__(self):
        # Inicializa a conexão com o banco de dados e o cursor
        self.conexao = sqlite3.connect("sistema_academico.db")  # Substitua pelo caminho correto do seu banco de dados
        self.cursor = self.conexao.cursor()

        # Cria a tabela cursos se ela não existir
        self.criar_tabela()

    def criar_tabela(self):
        try:
            # Criação da tabela cursos, caso ela não exista
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS cursos (
                    curso_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL
                )
            ''')
            self.conexao.commit()
            print("Tabela 'cursos' criada ou já existente.")
        except Exception as e:
            print(f"Erro ao criar a tabela cursos: {e}")

    def cadastrar(self, nome):
        try:
            self.cursor.execute("INSERT INTO cursos (nome) VALUES (?)", (nome,))
            self.conexao.commit()
            print(f"Curso '{nome}' cadastrado com sucesso.")
        except Exception as e:
            print(f"Erro ao cadastrar o curso: {e}")

    def excluir(self, curso_id):
        try:
            # Executa a exclusão com o ID do curso
            self.cursor.execute("DELETE FROM cursos WHERE curso_id = ?", (curso_id,))
            self.conexao.commit()  # Confirma a exclusão
            print(f"Curso com ID {curso_id} excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir o curso: {e}")

    def listar(self, tabela):
        # Exibe todos os cursos na tabela
        try:
            self.cursor.execute("SELECT curso_id, nome FROM cursos")
            rows = self.cursor.fetchall()
            tabela.delete(*tabela.get_children())  # Limpa a tabela antes de inserir novos dados
            for row in rows:
                tabela.insert("", "end", values=row)
        except Exception as e:
            print(f"Erro ao listar os cursos: {e}")
