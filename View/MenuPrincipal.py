import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from Models.Model import *
from Controllers.Teacher import *
from Controllers.Tasks import *
from Controllers.Course import *
from Controllers.Students import *
from View.Teste01 import *

menuPrincipal = ctk.CTk()
menuPrincipal.title("Menu Principal")
menuPrincipal.geometry("400x300")
ctk.set_appearance_mode("dark")
ctk.CTkLabel(menuPrincipal, text="Sistema de Cadastro", font=("Arial", 30)).pack(pady=20)

ctk.CTkButton(menuPrincipal, text="Alunos", command=tela_aluno, font=("Arial", 17)).pack(pady=10)
ctk.CTkButton(menuPrincipal, text="Professores", command=abrir_tela_professor, font=("Arial", 17)).pack(pady=10)

menuPrincipal.mainloop()
