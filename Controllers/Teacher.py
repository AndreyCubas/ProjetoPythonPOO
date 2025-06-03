from Models.Model import Teacher

def create_teacher():
    print("\n------ Cadastro de Professor ------")
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    password = input("Senha: ")
    siape = input("SIAPE: ")

    if Teacher.select().where(Teacher.siape == siape).exists():
        print(" Já existe um professor com esse SIAPE.")
        return

    teacher = Teacher.create(
        name=name,
        phone=phone,
        email=email,
        password=password,
        siape=siape
    )
    print(f"\n Professor {teacher.name} cadastrado com sucesso!\n")

def list_teachers():
    print("\n------ Lista de Professores ------")
    teachers = Teacher.select()

    if not teachers:
        print("Nenhum professor cadastrado.\n")
        return

    print(f"Total: {len(teachers)}\n")
    for teacher in teachers:
        print(f" Nome: {teacher.name} | SIAPE: {teacher.siape}")

def edit_teacher():
    list_teachers()
    siape = input("\nInforme o SIAPE do professor que será editado: ")
    
    try:
        teacher = Teacher.get(Teacher.siape == siape)

        print("\n--- Informe os novos dados ---")
        teacher.name = input("Nome: ")
        teacher.phone = input("Telefone: ")
        teacher.email = input("Email: ")
        teacher.password = input("Senha: ")
        teacher.siape = input("Novo SIAPE: ")
        teacher.save()

        print(f"\n Professor {teacher.name} editado com sucesso!\n")

    except Teacher.DoesNotExist:
        print(" Professor não encontrado.")

def delete_teacher():
    list_teachers()
    siape = input("\nInforme o SIAPE do professor que será deletado: ")
    
    try:
        teacher = Teacher.get(Teacher.siape == siape)
        teacher.delete_instance()
        print(f"\n Professor {teacher.name} removido com sucesso!\n")

    except Teacher.DoesNotExist:
        print(" Professor não encontrado.")
