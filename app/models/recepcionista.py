from app import db
class Recepcionista(db.Model):  
    __tablename__ = "recepcionista"
    nome = db.Column(db.String(100))
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(80))
    cpf = db.Column(db.String(11))
    senha = db.Column(db.String(20))
