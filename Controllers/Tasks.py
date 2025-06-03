from Models.Model import Task, Student, Course
from datetime import datetime

def create_task():
    print("\n------ Cadastro de Tarefa ------")
    registration = input("Matrícula do Aluno: ")
    course_id = input("ID do Curso: ")
    name = input("Título da Tarefa: ")
    description = input("Descrição: ")
    deadline_str = input("Data de entrega (AAAA-MM-DD): ")

    try:
        student = Student.get(Student.registration == registration)
        course = Course.get(Course.id == course_id)
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")

        task = Task.create(
            name=name,
            description=description,
            deadline=deadline,
            status="pendente",
            course=course,
            student=student
        )
        print(f"\nTarefa '{task.name}' criada com sucesso!\n")

    except Student.DoesNotExist:
        print("Estudante não encontrado.")
    except Course.DoesNotExist:
        print("Curso não encontrado.")
    except ValueError:
        print("Data inválida. Use o formato AAAA-MM-DD.")

def list_tasks():
    print("\n------ Lista de Tarefas ------")
    tasks = Task.select()

    if not tasks:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print(f"Total: {len(tasks)}\n")
    for task in tasks:
        print(f"ID: {task.id} | Nome: {task.name} | Aluno: {task.student.name} | Curso: {task.course.name} | Status: {task.status} | Entrega: {task.deadline.strftime('%d/%m/%Y')}")

def edit_task():
    list_tasks()
    task_id = input("\nInforme o ID da tarefa que será editada: ")

    try:
        task = Task.get(Task.id == task_id)

        print("\n--- Informe os novos dados da tarefa ---")
        task.name = input("Título: ")
        task.description = input("Descrição: ")
        deadline_str = input("Nova data de entrega (AAAA-MM-DD): ")
        task.status = input("Status (pendente/concluída): ")

        try:
            task.deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Mantendo a anterior.")

        task.save()
        print(f"\nTarefa '{task.name}' atualizada com sucesso!\n")

    except Task.DoesNotExist:
        print("Tarefa não encontrada.")

def delete_task():
    list_tasks()
    task_id = input("\nInforme o ID da tarefa que será deletada: ")

    try:
        task = Task.get(Task.id == task_id)
        task.delete_instance()
        print(f"\nTarefa '{task.name}' deletada com sucesso!\n")

    except Task.DoesNotExist:
        print("Tarefa não encontrada.")
