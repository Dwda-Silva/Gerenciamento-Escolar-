from database import Database

class Aluno:
    def __init__(self):
        self.db = Database()
        self.criar_tabela()

    def criar_tabela(self):
        query = """
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            cep TEXT NOT NULL,
            email TEXT NOT NULL,
            cpf TEXT NOT NULL
        )
        """
        self.db.execute(query)

    def cadastrar(self, nome, idade, cep, email, cpf):
        query = "INSERT INTO alunos (nome, idade, cep, email, cpf) VALUES (?, ?, ?, ?, ?)"
        self.db.execute(query, (nome, idade, cep, email, cpf))

    def listar(self, tabela):
        query = "SELECT * FROM alunos"
        alunos = self.db.fetch(query)

        # Limpar a tabela antes de adicionar novos dados
        for row in tabela.get_children():
            tabela.delete(row)

        for aluno in alunos:
            tabela.insert("", "end", values=aluno)

    def excluir(self, matricula):
        query = "DELETE FROM alunos WHERE matricula = ?"
        self.db.execute(query, (matricula,))
