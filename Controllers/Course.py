from Models import Model

def createCourse(current_professor):
    
    if current_professor is None:
        print("Este Curso está sem Professor!")
        return

    nome = input("Título: ")
    descricao = input("Descrição: ")
    conteudo = input("Conteúdo: ")

    # Criando o curso com que tenha o professor criado
    course = Course.create(
        name=nome,
        description=descricao,
        content=conteudo,
        teacher=current_professor
    )

    print(f"Curso '{course.name}' criado com sucesso para o professor {course.teacher}!")
    
def listCourses(courses):
    
    courses = Course.select()
    
    if(len(courses) == 0):
        print("Nenhum curso encontrado.")
        return
    else:
        print("\n------Cursos------")
        for couse in courses:
            print(f"Nome: {course.name}, Professor: {course.teacher.name},Descrição: {course.description}, Conteúdo: {course.content}")
        
def editCourse():
    
    while(True):
        
        print("------Menu de Edição de Curso------")
        print("1. Editar Nome")
        print("2. Editar Descrição")
        print("3. Editar Conteúdo")
        print("4. Voltar")
        
        option = input("Escolha uma opção: ")

        if option == "1":
            
            course_id = input("Digite o ID do curso que voce queira editar: ")
            Course.get_course_by_id(course_id)
            course.name = input("Digite o novo nome: ")
            course.save()
            print(f"Curso {course.name} editado com sucesso!")
            
        elif option == "2":
            
            course_id = input("Digite o ID do curso que voce queira editar: ")
            Course.get_course_by_id(course_id)
            course.description = input("Digite a nova descrição: ")
            course.save()
            print(f"Curso {course.name} editado com sucesso!")
            
        elif option == "3":
            
            course_id = input("Digite o ID do curso que voce queira editar: ")
            Course.get_course_by_id(course_id)
            course.content = input("Digite o novo conteúdo: ")
            course.save()
            print(f"Curso {course.name} editado com sucesso!")
            
        elif option == "4":
            
            break
    
        else:
            print("Opção inválida. Tente novamente.")
            
def deleteCourse():
    
    course_id = input("Digite o ID do curso que voce queira editar: ")
    Course.get_course_by_id(course_id)
    course.delete_instance()
    print(f"Curso {course.name} deletado com sucesso!")
    