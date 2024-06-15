from app import db
class Recepcionista(db.Model):  
    __tablename__ = "recepcionista"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))
    nome = db.Column(db.String(80))
