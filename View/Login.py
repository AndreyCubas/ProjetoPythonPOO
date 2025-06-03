from Models.Model import Student, Teacher

def login():
    from View.App import studentMenu, professorMenu
    print("\n=== LOGIN ===")
    user_id = input("RA (Estudante) ou SIAPE (Professor): ").strip()
    password = input("Senha: ").strip()

    student = Student.select().where(
        (Student.registration == user_id) & (Student.password == password)
    ).first()

    if student:
        print(f"\nBem-vindo(a), estudante {student.name}!")
        studentMenu(student)
        return

    professor = Teacher.select().where(
        (Teacher.siape == user_id) & (Teacher.password == password)
    ).first()

    if professor:
        print(f"\nBem-vindo(a), professor(a) {professor.name}!")
        professorMenu(professor)
        return

    print("\nUsuário ou senha inválidos.")
