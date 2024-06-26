from app import db
from sqlalchemy import DateTime
from sqlalchemy.dialects.mysql import NCHAR

class Log(db.Model):
    __tablename__ = "log"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hora = db.Column(DateTime)
    hash_log = db.Column(NCHAR(50))
