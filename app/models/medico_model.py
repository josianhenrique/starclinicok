from app import db
from sqlalchemy.orm import relationship

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    crm = db.Column(db.String(60), unique=True, nullable=False)
    especialidade_id = db.Column(db.Integer, db.ForeignKey('especialidade.id'))
    
    especialidade = relationship("Especialidade", back_populates="medicos")
    consultas = relationship('Consulta', back_populates='medico')
    
    
    def __init__(self, nome, telefone, cpf, crm, especialidade_id):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.crm = crm
        self.especialidade_id = especialidade_id

    def __repr__(self):
        return f'<Medico {self.nome}>'
