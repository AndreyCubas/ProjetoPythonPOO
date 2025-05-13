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

class Teacher(BaseModel):

    name = CharField()
    email = CharField()
    siape = CharField(unique=True)
    
class Course(BaseModel):

    name = CharField()
    description = TextField()
    teacher = ForeignKeyField(Teacher, backref='courses')
    description = CharField()
    content = CharField()

class Task(BaseModel):

    name = CharField()
    description = CharField()
    deadline = DateField()
    status = CharField(default="Pending")
    course = ForeignKeyField(Course, backref="tasks")

my_database.connect()
my_database.create_tables([Course, Task, Student])

