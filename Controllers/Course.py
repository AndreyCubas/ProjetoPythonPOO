from Models.Model import Course

def createCourse(current_professor):
    
    if current_professor is None:
        print("Este Curso está sem Professor!")
        return

    nome = input("Título: ")
    descricao = input("Descrição: ")
    conteudo = input("Conteúdo: ")

    course = Course.create(
        name=nome,
        description=descricao,
        content=conteudo,
        teacher=current_professor
    )

    print(f"Curso '{course.name}' criado com sucesso para o professor {course.teacher}!")
    
def listCourses():
    courses = Course.select()

    if not courses:
        print("Nenhum curso encontrado.")
        return

    print("\n------Cursos------")
    for course in courses:
        print(f"ID: {course.id} Nome: {course.name}, Professor: {course.teacher.name}, Descrição: {course.description}, Conteúdo: {course.content}")

        
def editCourse():
    while True:
        print("------Menu de Edição de Curso------")
        print("1. Editar Nome")
        print("2. Editar Descrição")
        print("3. Editar Conteúdo")
        print("4. Voltar")
        
        option = input("Escolha uma opção: ")

        if option in ["1", "2", "3"]:
            listCourses()
            course_id = input("Digite o ID do curso que você deseja editar: ")
            try:
                
                course = Course.get(Course.id == course_id)
            except Course.DoesNotExist:
                print("Curso não encontrado.")
                continue

            if option == "1":
                course.name = input("Digite o novo nome: ")
            elif option == "2":
                course.description = input("Digite a nova descrição: ")
            elif option == "3":
                course.content = input("Digite o novo conteúdo: ")

            course.save()
            print(f"Curso '{course.name}' editado com sucesso!")

        elif option == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
