import Models
import App
from datetime import date
from peewee import *

def login():
    print("\n=== LOGIN ===")
    user_id = input("RA (Estudante) ou SIAPE (Professor): ")
    password = input("Senha: ")
    
    student = Student.select().where(
        (Student.ra == user_id) & (Student.password == password)
    ).first()

    if student:
        print(f"\nBem-vindo(a), estudante {student.name}!")
        student_menu()
        return
    
    professor = Professor.select().where(
        (Professor.siape == user_id) & (Professor.password == password)
    ).first()

    if professor:
        print(f"\nBem-vindo(a), professor(a) {professor.name}!")
        professor_menu(professor)
        return

    print("\nUsuário ou senha inválidos.")
