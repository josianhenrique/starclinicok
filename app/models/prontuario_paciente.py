from app import db
class ProntuarioPaciente(db.Model):
    __tablename__ = 'prontuario_paciente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    historico = db.Column(db.String(80), nullable=False)
    nome  = db.Column(db.String(80))
    whatsapp = db.Column(db.String(10))
    email = db. Column(db.String(50))
    #consultas = db.relationship('Consulta', back_populates='prontuario_paciente')
    
    
    
    
    
