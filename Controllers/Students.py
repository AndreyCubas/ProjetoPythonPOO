from Models.Model import Student

def create_student():
    print("\n------ Cadastro de Estudante ------")
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    password = input("Senha: ")
    ra = input("Matrícula: ")

    if Student.select().where(Student.ra == ra).exists():
        print("Já existe um estudante com essa matrícula.")
        return

    student = Student.create(
        name=name,
        phone=phone,
        email=email,
        password=password,
        ra=ra
    )
    print(f"\ Estudante {student.name} cadastrado com sucesso!\n")

def list_students():
    students = Student.select()

    print("\n------ Lista de Estudantes ------")
    if not students:
        print("Nenhum estudante cadastrado.\n")
        return

    print(f"Total: {len(students)}\n")
    for student in students:
        print(f" Nome: {student.name} | Matrícula: {student.ra}")

def edit_student():
    ra = input("\nInforme a matrícula do estudante a ser editado: ")

    try:
        student = Student.get(Student.ra == ra)

        print("\n--- Informe os novos dados ---")
        student.name = input("Nome: ")
        student.phone = input("Telefone: ")
        student.email = input("Email: ")
        student.password = input("Senha: ")
        student.ra = input("Nova Matrícula: ")
        student.save()

        print(f"\n Estudante {student.name} atualizado com sucesso!\n")

    except Student.DoesNotExist:
        print(" Estudante não encontrado.")

def delete_student():
    ra = input("\nInforme a matrícula do estudante a ser deletado: ")

    try:
        student = Student.get(Student.ra == ra)
        student.delete_instance()
        print(f"\n Estudante {student.name} removido com sucesso!\n")

    except Student.DoesNotExist:
        print(" Estudante não encontrado.")
