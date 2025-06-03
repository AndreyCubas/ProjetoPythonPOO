from Models.Model import *
from Controllers.Teacher import *
from Controllers.Tasks import *
from Controllers.Course import *
from Controllers.Students import *
from View.Login import *

print("Bem Vindo Ao Sistema!")

def MenuGeral():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Login")
        print("2 - Criar Professor")
        print("3 - Criar Estudante")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            login()
        elif option == "2":
            create_teacher()
        elif option == "3":
            create_student()
        elif option == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def professorMenu(current_professor):
    while True:
        print("\n=== MENU DO PROFESSOR ===")
        print("1 - Gerenciar Estudantes")
        print("2 - Gerenciar Professores")
        print("3 - Gerenciar Cursos")
        print("4 - Gerenciar Tarefas")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            student_management()
        elif option == "2":
            teacher_management()
        elif option == "3":
            course_management(current_professor)
        elif option == "4":
            task_management()
        elif option == "0":
            print("Saindo do menu do professor...")
            break
        else:
            print("Opção inválida.")


def studentMenu(current_student):
    while True:
        print("\n=== MENU DO ESTUDANTE ===")
        print("1 - Listar Professores")
        print("2 - Listar Cursos")
        print("3 - Listar Tarefas")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            list_teachers()
        elif option == "2":
            listCourses()
        elif option == "3":
            list_tasks()
        elif option == "0":
            print("Saindo do menu do estudante...")
            break
        else:
            print("Opção inválida.")


def student_management():
    while True:
        print("\n--- GERENCIAMENTO DE ESTUDANTES ---")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Deletar")
        print("0 - Voltar")

        option = input("Opção: ")
        if option == "1":
            create_student()
        elif option == "2":
            list_students()
        elif option == "3":
            edit_student()
        elif option == "4":
            delete_student()
        elif option == "0":
            break
        else:
            print("Opção inválida.")


def teacher_management():
    while True:
        print("\n--- GERENCIAMENTO DE PROFESSORES ---")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Deletar")
        print("0 - Voltar")

        option = input("Opção: ")
        if option == "1":
            create_teacher()
        elif option == "2":
            list_teachers()
        elif option == "3":
            edit_teacher()
        elif option == "4":
            delete_teacher()
        elif option == "0":
            break
        else:
            print("Opção inválida.")


def course_management(current_professor):
    while True:
        print("\n--- GERENCIAMENTO DE CURSOS ---")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Deletar")
        print("0 - Voltar")

        option = input("Opção: ")
        if option == "1":
            createCourse(current_professor)
        elif option == "2":
            listCourses()
        elif option == "3":
            editCourse()
        elif option == "4":
            deleteCourse()
        elif option == "0":
            break
        else:
            print("Opção inválida.")


def task_management():
    while True:
        print("\n--- GERENCIAMENTO DE TAREFAS ---")
        print("1 - Criar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Deletar")
        print("0 - Voltar")

        option = input("Opção: ")
        if option == "1":
            create_task()
        elif option == "2":
            list_tasks()
        elif option == "3":
            edit_task()
        elif option == "4":
            delete_task()
        elif option == "0":
            break
        else:
            print("Opção inválida.")

MenuGeral()