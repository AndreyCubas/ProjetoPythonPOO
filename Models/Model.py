from peewee import *
from datetime import date

my_database = SqliteDatabase("my_data.db")

class BaseModel(Model):

    class Meta:
        
        database = my_database

class Student(BaseModel):

    name = CharField()
    registration = CharField(unique=True)
    email = CharField()
    
    def get_student_by_registration(registration):
        try:
            student = Student.get(Student.registration == registration)
            return student
        except Student.DoesNotExist:
            return None

class Teacher(BaseModel):

    name = CharField()
    email = CharField()
    siape = CharField(unique=True)
    
    def get_teacher_by_siape(siape):
        try:
            teacher = Teacher.get(Teacher.siape == siape)
            return teacher
        except Teacher.DoesNotExist:
            return None
    
class Course(BaseModel):

    name = CharField()
    teacher = ForeignKeyField(Teacher, backref='courses')
    description = CharField()
    content = CharField()
    
    def get_course_by_id(course_id):
        try:
            course = Course.get(Course.id == course_id)
            return course
        except Course.DoesNotExist:
            return None

class Task(BaseModel):

    name = CharField()
    description = CharField()
    deadline = DateField()
    status = CharField(default="Pending")
    course = ForeignKeyField(Course, backref="tasks")
    student = ForeignKeyField(Student, backref="tasks")
    
    def get_task_by_id(task_id):
        try:
            task = Task.get(Task.id == task_id)
            return task
        except Task.DoesNotExist:
            return None
        
    def get_tasks_by_student(student_id):
        try:
            tasks = Task.select().where(Task.student == student_id)
            return tasks
        except Task.DoesNotExist:
            return None
        

my_database.connect()
my_database.create_tables([Course, Task, Student])