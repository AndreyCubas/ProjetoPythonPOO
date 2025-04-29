from peewee import *
from datetime import date

myDataBase = SqliteDatabase("meus_dados.db")

class MinhaBase(Model):
    class Meta:
        Database = my

class Tarefas(MinhaBase):
    nome = CharField()
    descricao = CharField()
    prazo = DateField()
    status = CharField(default = "Pedente")
    curso = ForeignKeyField(Curso, backref= "Tarefas")

class Aluno(MinhaBase):
    nome = CharField()
    matricula = CharField(unique = True)

class Curso(MinhaBase):
    nome = CharField()
    descricao = TextField()



myDataBase.connect()
myDataBase.create_tables([])
