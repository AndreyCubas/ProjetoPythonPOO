from peewee import *

myDataBase = SqliteDatabase("meus_dados.db")

class MinhaBase(Model):
    class Meta:
        myDataBase = Database

class Produto(MinhaBase):
    



myDataBase.connect()
myDataBase.create_tables([])
