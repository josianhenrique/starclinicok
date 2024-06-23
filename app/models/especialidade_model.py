from app import db
from sqlalchemy.orm import relationship

class Especialidade(db.Model):
    __tablename__ = "especialidade"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80))
    
    medicos = relationship("Medico", back_populates="especialidade")
