import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import customtkinter as ctk
from Models.Model import Student, Teacher
import tkinter as tk
from tkinter import messagebox
from peewee import IntegrityError

def tela_aluno():
    ctk.set_appearance_mode("dark")
    janela_aluno = ctk.CTkToplevel()
    janela_aluno.title("Cadastro de Aluno")
    janela_aluno.geometry("760x460") 

    ctk.CTkLabel(janela_aluno, text="Tela de Aluno", font=("Arial", 30)).grid(row=0, column=0, columnspan=6, padx=(10, 5), pady=10, sticky="ew")
    
    ctk.CTkLabel(janela_aluno, text="Nome:").grid(row=1, column=0, padx=(5, 2), pady=5, sticky="e")
    entry_name = ctk.CTkEntry(janela_aluno, width=200)
    entry_name.grid(row=1, column=1, padx=(2, 5), pady=7, sticky="w")


    ctk.CTkLabel(janela_aluno, text="Telefone:").grid(row=2, column=0, padx=(5, 2), pady=5, sticky="e")
    entry_phone = ctk.CTkEntry(janela_aluno, width=200)
    entry_phone.grid(row=2, column=1, padx=(2, 5), pady=5, sticky="w")

    ctk.CTkLabel(janela_aluno, text="Email:").grid(row=3, column=0, padx=(5, 2), pady=5, sticky="e")
    entry_email = ctk.CTkEntry(janela_aluno, width=200)
    entry_email.grid(row=3, column=1, padx=(2, 5), pady=5, sticky="w")

    ctk.CTkLabel(janela_aluno, text="Senha:").grid(row=4, column=0, padx=(5, 2), pady=5, sticky="e")
    entry_password = ctk.CTkEntry(janela_aluno, show="*", width=200)
    entry_password.grid(row=4, column=1, padx=(2, 5), pady=5, sticky="w")

    ctk.CTkLabel(janela_aluno, text="Matrícula:").grid(row=5, column=0, padx=(5, 2), pady=5, sticky="e")
    entry_registration = ctk.CTkEntry(janela_aluno, width=200)
    entry_registration.grid(row=5, column=1, padx=(2, 5), pady=5, sticky="w")

    current_student_id = {'id': None}

    def limpar_campos():
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_registration.delete(0, tk.END)
        current_student_id['id'] = None
        btn_salvar.configure(text="Salvar")

    list_frame = tk.Frame(janela_aluno)
    list_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.grid(side=tk.RIGHT, fill=tk.Y)
    listbox = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
    listbox.grid(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    def load_students():
        listbox.delete(0, tk.END)
        for s in Student.select():
            listbox.insert(tk.END, f"{s.id} | {s.name} | {s.registration}")

    def on_list_select(event=None):
        listbox = tk.Listbox(janela_aluno, width=30, height=10)
        listbox.grid()


    def salvar_aluno():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        password = entry_password.get()
        registration = entry_registration.get()

        if not all([name, phone, email, password, registration]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            if current_student_id['id'] is None:
                novo_aluno = Student.create(name=name, phone=phone, email=email, password=password, registration=registration)
                messagebox.showinfo("Sucesso", f"Aluno {novo_aluno.name} salvo com sucesso!")
            else:
                s = Student.get_by_id(current_student_id['id'])
                s.name = name
                s.phone = phone
                s.email = email
                s.password = password
                s.registration = registration
                s.save()
                messagebox.showinfo("Sucesso", f"Aluno {s.name} atualizado com sucesso!")
        except IntegrityError as erro:
            messagebox.showerror("Erro", f"Falha ao salvar: {erro}")
        limpar_campos()
        load_students()

    def editar_selecionado():
        on_list_select()

    def excluir_selecionado():
        sel = listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Nenhum registro selecionado.")
            return
        val = listbox.get(sel[0])
        sid = int(val.split('|')[0].strip())
        if messagebox.askyesno("Confirma", "Deseja excluir este aluno?"):
            s = Student.get_by_id(sid)
            s.delete_instance()
            limpar_campos()
            load_students()

    lb_botoes = ctk.CTkFrame(janela_aluno)
    lb_botoes.grid(row=6, column=0, columnspan=2, pady=5)
    btn_salvar = ctk.CTkButton(lb_botoes, text="Salvar", command=salvar_aluno)
    btn_salvar.grid(side="left", padx=6)
    btn_limpar = ctk.CTkButton(lb_botoes, text="Limpar", command=limpar_campos)
    btn_limpar.grid(side="left", padx=6)
    btn_editar = ctk.CTkButton(lb_botoes, text="Editar", command=editar_selecionado)
    btn_editar.grid(side="left", padx=6)
    btn_excluir = ctk.CTkButton(lb_botoes, text="Excluir", command=excluir_selecionado)
    btn_excluir.grid(side="left", padx=6)
    btn_atualizar = ctk.CTkButton(lb_botoes, text="Atualizar Lista", command=load_students)
    btn_atualizar.grid(side="left", padx=6)

    load_students()

def abrir_tela_professor():
    ctk.set_appearance_mode("dark")
    janela_professor = ctk.CTkToplevel()
    janela_professor.title("Cadastro de Professor")
    janela_professor.geometry("650x950")

    ctk.CTkLabel(janela_professor, text="Tela de Professor").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    ctk.CTkLabel(janela_professor, text="Nome:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_name_prof = ctk.CTkEntry(janela_professor, width=200)
    entry_name_prof.grid(row=1, column=1, padx=10, pady=10)

    ctk.CTkLabel(janela_professor, text="Telefone:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_phone_prof = ctk.CTkEntry(janela_professor, width=200)
    entry_phone_prof.grid(row=2, column=1, padx=10, pady=10)

    ctk.CTkLabel(janela_professor, text="Email:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_email_prof = ctk.CTkEntry(janela_professor, width=200)
    entry_email_prof.grid(row=3, column=1, padx=10, pady=10)

    ctk.CTkLabel(janela_professor, text="Senha:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_password_prof = ctk.CTkEntry(janela_professor, show="*", width=200)
    entry_password_prof.grid(row=4, column=1, padx=10, pady=10)

    ctk.CTkLabel(janela_professor, text="SIAPE:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
    entry_siape_prof = ctk.CTkEntry(janela_professor, width=200)
    entry_siape_prof.grid(row=5, column=1, padx=10, pady=10)

    current_prof_id = {'id': None}

    def limpar_campos_professor():
        entry_name_prof.delete(0, tk.END)
        entry_phone_prof.delete(0, tk.END)
        entry_email_prof.delete(0, tk.END)
        entry_password_prof.delete(0, tk.END)
        entry_siape_prof.delete(0, tk.END)
        current_prof_id['id'] = None
        btn_salvar_prof.configure(text="Salvar")

    list_frame = tk.Frame(janela_professor)
    list_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.grid(side=tk.RIGHT, fill=tk.Y)
    listbox = tk.Listbox(list_frame, height=8, yscrollcommand=scrollbar.set)
    listbox.grid(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    def load_professors():
        listbox.delete(0, tk.END)
        for p in Teacher.select():
            listbox.insert(tk.END, f"{p.id} | {p.name} | {p.siape}")

    def on_prof_select(event=None):
        sel = listbox.curselection()
        if not sel:
            return
        val = listbox.get(sel[0])
        pid = int(val.split('|')[0].strip())
        p = Teacher.get_by_id(pid)
        entry_name_prof.delete(0, tk.END); entry_name_prof.insert(0, p.name)
        entry_phone_prof.delete(0, tk.END); entry_phone_prof.insert(0, p.phone)
        entry_email_prof.delete(0, tk.END); entry_email_prof.insert(0, p.email)
        entry_password_prof.delete(0, tk.END); entry_password_prof.insert(0, p.password)
        entry_siape_prof.delete(0, tk.END); entry_siape_prof.insert(0, p.siape)
        current_prof_id['id'] = p.id
        btn_salvar_prof.configure(text="Atualizar")

    def salvar_professor():
        name = entry_name_prof.get()
        phone = entry_phone_prof.get()
        email = entry_email_prof.get()
        password = entry_password_prof.get()
        siape = entry_siape_prof.get()

        if not all([name, phone, email, password, siape]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            if current_prof_id['id'] is None:
                novo_professor = Teacher.create(name=name, phone=phone, email=email, password=password, siape=siape)
                messagebox.showinfo("Sucesso", f"Professor {novo_professor.name} salvo com sucesso!")
            else:
                p = Teacher.get_by_id(current_prof_id['id'])
                p.name = name
                p.phone = phone
                p.email = email
                p.password = password
                p.siape = siape
                p.save()
                messagebox.showinfo("Sucesso", f"Professor {p.name} atualizado com sucesso!")
        except IntegrityError as erro:
            messagebox.showerror("Erro", f"Falha ao salvar: {erro}")
        limpar_campos_professor()
        load_professors()

    def editar_prof_selecionado():
        on_prof_select()

    def excluir_prof_selecionado():
        sel = listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Nenhum registro selecionado.")
            return
        val = listbox.get(sel[0])
        pid = int(val.split('|')[0].strip())
        if messagebox.askyesno("Confirma", "Deseja excluir este professor?"):
            p = Teacher.get_by_id(pid)
            p.delete_instance()
            limpar_campos_professor()
            load_professors()

    lb_botoes_prof = ctk.CTkFrame(janela_professor)
    lb_botoes_prof.grid(row=6, column=0, columnspan=2, pady=5)
    btn_salvar_prof = ctk.CTkButton(lb_botoes_prof, text="Salvar", command=salvar_professor)
    btn_salvar_prof.grid(side="left", padx=6)
    btn_limpar_prof = ctk.CTkButton(lb_botoes_prof, text="Limpar", command=limpar_campos_professor)
    btn_limpar_prof.grid(side="left", padx=6)
    btn_editar_prof = ctk.CTkButton(lb_botoes_prof, text="Editar", command=editar_prof_selecionado)
    btn_editar_prof.grid(side="left", padx=6)
    btn_excluir_prof = ctk.CTkButton(lb_botoes_prof, text="Excluir", command=excluir_prof_selecionado)
    btn_excluir_prof.grid(side="left", padx=6)
    btn_atualizar_prof = ctk.CTkButton(lb_botoes_prof, text="Atualizar Lista", command=load_professors)
    btn_atualizar_prof.grid(side="left", padx=6)

    load_professors()


menuPrincipal = ctk.CTk()
menuPrincipal.title("Menu Principal")
menuPrincipal.geometry("600x500")
ctk.set_appearance_mode("dark")
ctk.CTkLabel(menuPrincipal, text="Sistema de Cadastro", font=("Arial", 30)).grid(pady=20)

ctk.CTkButton(menuPrincipal, text="Alunos", command=tela_aluno, font=("Arial", 17)).grid(pady=10)
ctk.CTkButton(menuPrincipal, text="Professores", command=abrir_tela_professor, font=("Arial", 17)).grid(pady=10)

menuPrincipal.mainloop()
