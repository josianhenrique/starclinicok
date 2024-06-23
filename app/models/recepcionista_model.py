from app import db
from sqlalchemy.orm import relationship

class Recepcionista(db.Model):
    __tablename__ = 'recepcionista'
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(10), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    
    consultas = relationship("Consulta", back_populates="recepcionista")

    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def __repr__(self):
        return f'<Recepcionista {self.nome}>'