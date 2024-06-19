from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import DateTime
from sqlalchemy.dialects.mysql import NCHAR

class Log(db.Model):
    __tablename__ = "log"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    #Date
    hora  = db.Column(DateTime)
    #Time
    hash_log = db.Column(NCHAR(50))
