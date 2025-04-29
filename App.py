import Models
from datetime import date
from peewee import *

print("Bem Vindo Ao Sistema!")

def MenuAlunos():

    print("\n---Menu Alunos---")
    print("1 - Adicionar Alunos")
    print("2 - Listar Aluno")
    print("3 - Atualizar Aluno")
    print("4 - Excluir Aluno")
    print("0 - Voltar")

    op = input("Escolha: ")
    if op == "1":
        nome = input("Nome: ")
        matricula = input("Matricula: ")
    
    elif op == "2":
        print("\n---Lista de Alunos---")
        for aluno in Models.aluno.alunos.select():
            print(f"{aluno.id} - {aluno.nome} - ({aluno.matricula})")

    elif op == "3":
        aluno.id = int(input("ID do ALuno a Atualizar: "))
        aluno = Models.aluno.get_by_id(alunoId)

