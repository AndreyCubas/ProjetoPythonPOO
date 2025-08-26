import customtkinter as ctk
from Controllers.Students import *
from Models.Model import Student
import tkinter as tk
from tkinter import messagebox

def tela_aluno():
    ctk.set_appearance_mode("dark")
    janela_aluno = ctk.CTkToplevel()
    janela_aluno.title("Cadastro de Aluno")
    janela_aluno.geometry("300x200")

    ctk.CTkLabel(janela_aluno, text="Tela de Aluno").grid(row=0, column=0, padx=5, pady=5)
    
    ctk.CTkLabel(janela_aluno, text="Nome:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    name = entry_name = ctk.CTkEntry(janela_aluno, width=200)
    name.grid(row=1, column=1, padx=10, pady=10)
    if(not name ):
        messagebox.showerror("Erro", "Por favor, preencha o nome.")
        return

    ctk.CTkLabel(janela_aluno, text="Telefone:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    phone = entry_phone = ctk.CTkEntry(janela_aluno, width=200)
    phone.grid(row=2, column=1, padx=10, pady=10)
    if(not phone ):
        messagebox.showerror("Erro", "Por favor, preencha o telefone.")
        return

    ctk.CTkLabel(janela_aluno, text="Email:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    email = entry_email = ctk.CTkEntry(janela_aluno, width=200)
    email.grid(row=3, column=1, padx=10, pady=10)
    if(not email ):
        messagebox.showerror("Erro", "Por favor, preencha o email.")
        return


    ctk.CTkLabel(janela_aluno, text="Senha:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
    password = entry_password = ctk.CTkEntry(janela_aluno, show="*", width=200)
    password.grid(row=4, column=1, padx=10, pady=10)
    if(not password ):
        messagebox.showerror("Erro", "Por favor, preencha a senha.")
        return

    ctk.CTkLabel(janela_aluno, text="Matrícula:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
    registration = entry_registration = ctk.CTkEntry(janela_aluno, width=200)
    registration.grid(row=5, column=1, padx=10, pady=10)
    if(not registration ):
        messagebox.showerror("Erro", "Por favor, preencha a matrícula.")
        return
    def limpar_campos():
        name.delete(0, tk.END)
        phone.delete(0, tk.END)
        email.delete(0, tk.END)
        password.delete(0, tk.END)
        registration.delete(0, tk.END)

    def salvar_aluno():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        password = entry_password.get()
        registration = entry_registration.get()

        novo_aluno = Student(name=name, phone=phone, email=email, password=password, registration=registration)
        controller = StudentsController()
        controller.create_student(novo_aluno)
        messagebox.showinfo(f"Aluno {novo_aluno.name} salvo com sucesso!")
        limpar_campos()
    lb_botoes = ctk.CTkFrame(janela_aluno)
    lb_botoes.grid(row=6, column=0, columnspan=2, pady=20)

    

def abrir_tela_professor():
    janela_professor = ctk.CTkToplevel()
    janela_professor.title("Cadastro de Professor")
    janela_professor.geometry("600x400")
    ctk.CTkLabel(janela_professor, text="Tela de Professor").pack(pady=10)

menuPrincipal = ctk.CTk()
menuPrincipal.title("Menu Principal")
menuPrincipal.geometry("400x300")

ctk.set_appearance_mode("dark")
ctk.CTkLabel(menuPrincipal, text="Sistema de Cadastro", font=("Arial", 30)).pack(pady=20)

ctk.CTkButton(menuPrincipal, text="Alunos", command=tela_aluno, font=("Arial", 17)).pack(pady=10)
ctk.CTkButton(menuPrincipal, text="Professores", command=abrir_tela_professor, font=("Arial", 17)).pack(pady=10)

menuPrincipal.mainloop()
