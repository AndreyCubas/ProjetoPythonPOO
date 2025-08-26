import tkinter as tk
from tkinter import messagebox
from peewee import *

# =========================
# Configuração do Banco
# =========================
db = SqliteDatabase("escola.db")

class BaseModel(Model):
    class Meta:
        database = db

class Estudante(BaseModel):
    nome = CharField()
    matricula = CharField(unique=True)
    curso = CharField()

db.connect()
db.create_tables([Estudante])

# =========================
# Interface Tkinter
# =========================
class CadastroEstudante:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Estudante")

        # Labels e Entrys
        tk.Label(master, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(master, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Matrícula:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_matricula = tk.Entry(master, width=30)
        self.entry_matricula.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Curso:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_curso = tk.Entry(master, width=30)
        self.entry_curso.grid(row=2, column=1, padx=5, pady=5)

        # Botões
        self.btn_salvar = tk.Button(master, text="Salvar", command=self.salvar)
        self.btn_salvar.grid(row=3, column=0, padx=5, pady=5)

        self.btn_limpar = tk.Button(master, text="Limpar", command=self.limpar)
        self.btn_limpar.grid(row=3, column=1, padx=5, pady=5)

        # Listbox
        self.listbox = tk.Listbox(master, width=60)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Botões da lista
        self.btn_editar = tk.Button(master, text="Editar", command=self.editar)
        self.btn_editar.grid(row=5, column=0, padx=5, pady=5)

        self.btn_excluir = tk.Button(master, text="Excluir", command=self.excluir)
        self.btn_excluir.grid(row=5, column=1, padx=5, pady=5)

        self.btn_atualizar = tk.Button(master, text="Atualizar", command=self.carregar_lista)
        self.btn_atualizar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.registro_editando = None  # guarda ID para edição
        self.carregar_lista()

    # =========================
    # Funções CRUD
    # =========================
    def salvar(self):
        nome = self.entry_nome.get().strip()
        matricula = self.entry_matricula.get().strip()
        curso = self.entry_curso.get().strip()

        if not nome or not matricula or not curso:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            if self.registro_editando:  # Atualizar registro
                estudante = Estudante.get_by_id(self.registro_editando)
                estudante.nome = nome
                estudante.matricula = matricula
                estudante.curso = curso
                estudante.save()
                messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
                self.registro_editando = None
                self.btn_salvar.config(text="Salvar")
            else:  # Criar novo registro
                Estudante.create(nome=nome, matricula=matricula, curso=curso)
                messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
        except IntegrityError:
            messagebox.showerror("Erro", "Já existe um estudante com essa matrícula!")
        self.limpar()
        self.carregar_lista()

    def limpar(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_curso.delete(0, tk.END)
        self.registro_editando = None
        self.btn_salvar.config(text="Salvar")

    def carregar_lista(self):
        self.listbox.delete(0, tk.END)
        for estudante in Estudante.select():
            self.listbox.insert(tk.END, f"{estudante.id} - {estudante.nome} | {estudante.matricula} | {estudante.curso}")

    def editar(self):
        try:
            selecionado = self.listbox.get(self.listbox.curselection())
            id_registro = int(selecionado.split(" - ")[0])
            estudante = Estudante.get_by_id(id_registro)

            # Preencher os campos
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, estudante.nome)

            self.entry_matricula.delete(0, tk.END)
            self.entry_matricula.insert(0, estudante.matricula)

            self.entry_curso.delete(0, tk.END)
            self.entry_curso.insert(0, estudante.curso)

            self.registro_editando = estudante.id
            self.btn_salvar.config(text="Atualizar")
        except:
            messagebox.showwarning("Atenção", "Selecione um registro para editar.")

    def excluir(self):
        try:
            selecionado = self.listbox.get(self.listbox.curselection())
            id_registro = int(selecionado.split(" - ")[0])
            estudante = Estudante.get_by_id(id_registro)
            estudante.delete_instance()
            messagebox.showinfo("Sucesso", "Registro excluído!")
            self.carregar_lista()
        except:
            messagebox.showwarning("Atenção", "Selecione um registro para excluir.")

# =========================
# Execução
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroEstudante(root)
    root.mainloop()
