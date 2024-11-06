from database import Database
import tkinter as tk
from tkinter import ttk
from aluno import Aluno
from curso import Curso
from turma import Turma
from polo_academico import PoloAcademico

# Interface para Alunos
class InterfaceAluno:
    def __init__(self, root):
        self.aluno = Aluno()

    def abrir_cadastro(self):
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro de Alunos")

        tk.Label(cadastro_window, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        nome_entry = tk.Entry(cadastro_window, width=40)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Idade:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        idade_entry = tk.Entry(cadastro_window, width=40)
        idade_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="CEP:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        cep_entry = tk.Entry(cadastro_window, width=40)
        cep_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        email_entry = tk.Entry(cadastro_window, width=40)
        email_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="CPF:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        cpf_entry = tk.Entry(cadastro_window, width=40)
        cpf_entry.grid(row=4, column=1, padx=5, pady=5)

        def cadastrar():
            nome = nome_entry.get()
            idade = idade_entry.get()
            cep = cep_entry.get()
            email = email_entry.get()
            cpf = cpf_entry.get()
            self.aluno.cadastrar(nome, idade, cep, email, cpf)
            limpar_campos_aluno()
            listar()

        def limpar_campos_aluno():
            nome_entry.delete(0, tk.END)
            idade_entry.delete(0, tk.END)
            cep_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            cpf_entry.delete(0, tk.END)

        tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).grid(row=5, column=1, pady=10)

        tabela = ttk.Treeview(cadastro_window, columns=("Matrícula", "Nome", "Idade", "CEP", "Email", "CPF"), show='headings')
        tabela.heading("Matrícula", text="Matrícula")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Idade", text="Idade")
        tabela.heading("CEP", text="CEP")
        tabela.heading("Email", text="Email")
        tabela.heading("CPF", text="CPF")
        tabela.grid(row=6, column=0, columnspan=2)

        def listar():
            self.aluno.listar(tabela)

        tk.Button(cadastro_window, text="Listar Alunos", command=listar).grid(row=5, column=0, pady=10)
        tk.Button(cadastro_window, text="Excluir Aluno", command=lambda: self.excluir_aluno(tabela)).grid(row=7, column=0, pady=10)
        tk.Button(cadastro_window, text="Voltar", command=cadastro_window.destroy).grid(row=7, column=1, pady=10)

    def excluir_aluno(self, tabela):
        try:
            selecionado = tabela.selection()[0]
            matricula = tabela.item(selecionado)['values'][0]
            self.aluno.excluir(matricula)
            self.aluno.listar(tabela)
        except IndexError:
            tk.messagebox.showerror("Erro", "Selecione um aluno para excluir.")


# Interface para Cursos
class InterfaceCurso:
    def __init__(self, root):
        self.curso = Curso()

    def abrir_cadastro(self):
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro de Cursos")

        tk.Label(cadastro_window, text="Nome do Curso:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        nome_entry = tk.Entry(cadastro_window, width=40)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        def cadastrar():
            nome = nome_entry.get()
            self.curso.cadastrar(nome)

        tk.Button(cadastro_window, text="Cadastrar Curso", command=cadastrar).grid(row=1, column=1, pady=10)

        tabela = ttk.Treeview(cadastro_window, columns=("Curso_ID", "Nome"), show='headings')
        tabela.heading("Curso_ID", text="ID")
        tabela.heading("Nome", text="Nome")
        tabela.grid(row=2, column=0, columnspan=2)

        def excluir_curso():
            try:
                selecionado = tabela.selection()[0]
                curso_id = tabela.item(selecionado)['values'][0]  # Obtém o curso_id da linha selecionada
                self.curso.excluir(curso_id)  # Chama o metodo excluir com o curso_id
                tabela.delete(selecionado)  # Remove a linha da tabela visualmente
                listar()  # Atualiza a tabela após a exclusão
            except IndexError:
                tk.messagebox.showerror("Erro", "Selecione um curso para excluir.")
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao excluir curso: {e}")

        def listar():
            self.curso.listar(tabela)

        tk.Button(cadastro_window, text="Listar Cursos", command=listar).grid(row=3, column=0, pady=10)
        tk.Button(cadastro_window, text="Excluir Curso", command=excluir_curso).grid(row=3, column=1, pady=10)
        tk.Button(cadastro_window, text="Voltar", command=cadastro_window.destroy).grid(row=4, column=1, pady=10)


# Interface para Turmas
class InterfaceTurma:
    def __init__(self, root):
        self.turma = Turma()

    def abrir_cadastro(self):
        cadastro_window = tk.Toplevel(root)
        cadastro_window.title("Cadastro de Turmas")

        tk.Label(cadastro_window, text="Nome da Turma:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        nome_entry = tk.Entry(cadastro_window, width=40)
        nome_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(cadastro_window, text="Curso:").grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # ComboBox para selecionar o nome do curso
        curso_nome_combobox = ttk.Combobox(cadastro_window, width=37)
        curso_nome_combobox.grid(row=1, column=1, padx=5, pady=5)

        # Carregar os cursos (nomes) na ComboBox
        cursos = self.carregar_cursos()
        curso_nome_combobox['values'] = [curso['nome'] for curso in cursos]

        tk.Label(cadastro_window, text="Turno:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        turno_entry = tk.Entry(cadastro_window, width=40)
        turno_entry.grid(row=2, column=1, padx=5, pady=5)

        def cadastrar():
            nome = nome_entry.get()
            curso_nome = curso_nome_combobox.get()  # Nome do curso selecionado
            turno = turno_entry.get()

            # Obter o curso_id a partir do nome do curso
            curso_id = self.get_curso_id_by_nome(curso_nome)
            if curso_id:
                self.turma.cadastrar(nome, curso_id, turno)
            else:
                tk.messagebox.showerror("Erro", "Curso não encontrado.")

        tk.Button(cadastro_window, text="Cadastrar Turma", command=cadastrar).grid(row=3, column=1, pady=10)

        tabela = ttk.Treeview(cadastro_window, columns=("Turma_ID", "Nome", "Curso_ID", "Turno"), show='headings')
        tabela.heading("Turma_ID", text="ID")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Curso_ID", text="Curso ID")
        tabela.heading("Turno", text="Turno")
        tabela.grid(row=4, column=0, columnspan=2)

        def listar():
            self.turma.listar(tabela)

        tk.Button(cadastro_window, text="Listar Turmas", command=listar).grid(row=5, column=0, pady=10)

        # Alteração aqui para pegar o turma_id corretamente
        def excluir_turma():
            try:
                selecionado = tabela.selection()[0]
                turma_id = tabela.item(selecionado)['values'][0]  # Obtendo o turma_id corretamente
                self.turma.excluir(turma_id)  # Passando o turma_id para excluir
                listar()  # Atualizando a lista após exclusão
            except IndexError:
                tk.messagebox.showerror("Erro", "Selecione uma turma para excluir.")

        tk.Button(cadastro_window, text="Excluir Turma", command=excluir_turma).grid(row=5, column=1, pady=10)

        tk.Button(cadastro_window, text="Voltar", command=cadastro_window.destroy).grid(row=6, column=1, pady=10)

    def carregar_cursos(self):
        # Consulta ao banco para pegar cursos (nomes)
        db = Database()
        db.execute("SELECT curso_id, nome FROM cursos")
        cursos = [{'curso_id': row[0], 'nome': row[1]} for row in db.cursor.fetchall()]
        db.close()
        return cursos

    def get_curso_id_by_nome(self, nome):
        # Retorna o curso_id correspondente ao nome do curso
        db = Database()
        db.execute("SELECT curso_id FROM cursos WHERE nome = ?", (nome,))
        result = db.cursor.fetchone()
        db.close()
        if result:
            return result[0]  # Retorna o curso_id
        return None

class InterfacePoloAcademico:
    def __init__(self, root):
        self.db = Database()  # Conexão com o banco de dados
        self.root = root

    def abrir_gerenciamento(self):
        gerenciamento_window = tk.Toplevel(self.root)
        gerenciamento_window.title("Gerenciamento Polo Acadêmico")

        # Tabela para exibir os dados
        tabela = ttk.Treeview(gerenciamento_window, columns=("Matrícula", "Nome", "Turma", "Curso"), show="headings")
        tabela.heading("Matrícula", text="Matrícula")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Turma", text="Turma")
        tabela.heading("Curso", text="Curso")
        tabela.grid(row=0, column=0, padx=10, pady=10)

        # Função para carregar os dados
        def carregar_dados():
            try:
                # Realiza a consulta no banco de dados
                self.db.execute("""
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

                """)
                dados = self.db.cursor.fetchall()

                # Limpa a tabela antes de inserir os novos dados
                for item in tabela.get_children():
                    tabela.delete(item)

                # Insere os dados na tabela
                for row in dados:
                    tabela.insert("", "end", values=row)
            except Exception as e:
                tk.messagebox.showerror("Erro", f"Erro ao carregar os dados: {e}")

        # Botão para carregar os dados
        tk.Button(gerenciamento_window, text="Carregar Dados", command=carregar_dados).grid(row=1, column=0, pady=10)

        # Botão para voltar
        tk.Button(gerenciamento_window, text="Voltar", command=gerenciamento_window.destroy).grid(row=2, column=0, pady=10)

# Janela principal
root = tk.Tk()  # Crie a janela principal 'root' aqui, antes de qualquer outra coisa
root.title("Sistema Acadêmico")

# Criando os objetos das interfaces
interface_aluno = InterfaceAluno(root)
interface_curso = InterfaceCurso(root)
interface_turma = InterfaceTurma(root)

# Agora cria a interface do Polo Acadêmico antes de associá-la ao botão
interface_polo_academico = InterfacePoloAcademico(root)

# Adicionando os botões
tk.Button(root, text="Alunos", command=interface_aluno.abrir_cadastro).pack(padx=10, pady=10)
tk.Button(root, text="Cursos", command=interface_curso.abrir_cadastro).pack(padx=10, pady=10)
tk.Button(root, text="Turmas", command=interface_turma.abrir_cadastro).pack(padx=10, pady=10)

# **Passando a função diretamente** (Sem criar a instância no `command`):
tk.Button(root, text="Polo Acadêmico", command=interface_polo_academico.abrir_gerenciamento).pack(padx=10, pady=10)

# Iniciando o loop da interface
root.mainloop()

