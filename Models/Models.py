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
    
class Course(BaseModel):

    name = CharField()
    description = TextField()

class Task(BaseModel):

    name = CharField()
    description = CharField()
    deadline = DateField()
    status = CharField(default="Pending")
    course = ForeignKeyField(Course, backref="tasks")

class Teacher(BaseModel):

    name = CharField()
    email = CharField()
    siape = CharField(unique=True)

my_database.connect()
my_database.create_tables([Course, Task, Student])

