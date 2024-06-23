from app import db
from sqlalchemy.orm import relationship


class ProntuarioPaciente(db.Model):
    __tablename__ = 'prontuario_paciente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    historico = db.Column(db.String(800), nullable=False)
    nome = db.Column(db.String(80))
    whatsapp = db.Column(db.String(15))
    email = db.Column(db.String(50))
    
    consultas = relationship("Consulta", back_populates="prontuario_paciente") 
    

    
    
    
