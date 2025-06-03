from peewee import *
from datetime import date

my_database = SqliteDatabase("my_data.db")

class BaseModel(Model):

    class Meta:
        
        database = my_database

class Student(BaseModel):

    name = CharField()
    registration = CharField(unique=True)
    password = CharField()
    email = CharField()
    


class Teacher(BaseModel):

    name = CharField()
    email = CharField()
    siape = CharField(unique=True)
    phone = CharField(unique = True)
    password = CharField(   )
    

    
class Course(BaseModel):

    name = CharField()
    teacher = ForeignKeyField(Teacher, backref='courses')
    description = CharField()
    content = CharField()
    


class Task(BaseModel):

    name = CharField()
    description = CharField()
    deadline = DateField()
    status = CharField(default="Pending")
    course = ForeignKeyField(Course, backref="tasks")
    student = ForeignKeyField(Student, backref="tasks")
    
my_database.connect()
my_database.create_tables([Course,Teacher, Task, Student])