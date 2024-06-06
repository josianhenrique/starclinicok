from app import db
class ProntuarioPaciente(db.Model):
    __tablename__ = 'prontuario_paciente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    historico = db.Column(db.String(200), nullable=False)
    
    # Chave estrangeira para Paciente
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    
    # Relacionamento 1:1 com Paciente
    paciente = db.relationship('Paciente', back_populates='paciente')
    
