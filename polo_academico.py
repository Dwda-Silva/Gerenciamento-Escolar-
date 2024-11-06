from database import Database
import tkinter as tk

class PoloAcademico:
    def __init__(self):
        self.db = Database()  # A classe Database para interação com o banco

    def listar_polo(self, tabela):
        """
        Listar os alunos, suas turmas e cursos na tabela.
        """
        tabela.delete(*tabela.get_children())  # Limpa a tabela
        query = """
                SELECT 
    a.nome AS aluno_nome,
    t.nome AS turma_nome,
    c.nome AS curso_nome
FROM 
    alunos a
JOIN 
    alunos_turmas at ON id = at.aluno_id
JOIN 
    turmas t ON at.turma_id = t.turma_id
JOIN 
    cursos c ON t.curso_id = c.curso_id;

        """
        self.db.execute(query)
        rows = self.db.cursor.fetchall()
        for row in rows:
            tabela.insert("", "end", values=row)  # Insere os dados na tabela
