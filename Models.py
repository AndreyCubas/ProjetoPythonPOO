from peewee import *
from datetime import date

myDataBase = SqliteDatabase("meus_dados.db")

class MinhaBase(Model):
    class Meta:
        Database = myDataBase

class aluno(MinhaBase):
    nome = CharField()
    matricula = CharField(unique = True)

    def __str__(self):
        return f"Aluno: {self.nome} Matricula: {self.matricula}"
    
class curso(MinhaBase):
    nome = CharField()
    descricao = TextField()

class tarefas(MinhaBase):
    nome = CharField()
    descricao = CharField()
    prazo = DateField()
    status = CharField(default = "Pedente")
    curso = ForeignKeyField(curso, backref= "Tarefas")



myDataBase.connect()
myDataBase.create_tables([curso, tarefas, aluno])
