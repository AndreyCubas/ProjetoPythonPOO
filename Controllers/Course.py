import Models from Model


def createCourse(current_professor):
    if current_professor is None:
        print("Este Curso está sem Professor!")
        return

    nome = input("Título: ")
    descricao = input("Descrição: ")
    conteudo = input("Conteúdo: ")

    # Criando o curso com o professor associado
    course = course.create(
        name=nome,
        description=descricao,
        content=conteudo,
        teacher=current_professor
    )

    print(f"Curso '{course.name}' criado com sucesso para o professor {
          current_professor.name}!")
