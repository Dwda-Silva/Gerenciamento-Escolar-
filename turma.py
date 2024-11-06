import tkinter as tk
import sqlite3
from database import Database

class Turma:
    def __init__(self):
        self.db = Database()
        self.conexao = sqlite3.connect("sistema_academico.db")  # Substitua pelo caminho correto do seu banco de dados
        self.cursor = self.conexao.cursor()

    def cadastrar(self, nome, curso_id, turno):
        try:
            # Utiliza a instância do banco de dados para executar o comando
            self.db.execute("INSERT INTO turmas (nome, curso_id, turno) VALUES (?, ?, ?)", (nome, curso_id, turno))
            print(f"Turma '{nome}' cadastrada com sucesso.")
        except Exception as e:
            print(f"Erro ao cadastrar a turma: {e}")

    def listar(self, tabela):
        db = self.db
        db.execute("SELECT * FROM turmas")
        for row in db.cursor.fetchall():
            tabela.insert("", tk.END, values=row)
        db.close()

    def excluir(self, turma_id):
        db = self.db
        db.execute("DELETE FROM turmas WHERE turma_id=?", (turma_id,))
        db.connection.commit()  # Chama commit na conexão
        db.close()