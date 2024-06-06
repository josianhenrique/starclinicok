from app import db
class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data = db.Column(db.String(10), unique=True, nullable=False)

    # Relacionamento 1:1 com ProntuarioPaciente
    prontuario = db.relationship('prontuario_paciente', uselist=False, back_populates='prontuario_paciente')
    
