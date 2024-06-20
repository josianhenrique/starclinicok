from app import db

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(12), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    crm = db.Column(db.String(60), unique=True, nullable=False)
    fk_especialidade_id= db.Column(db.Integer,db.ForeignKey('especialidade.id'))

    def __init__(self, nome, telefone, cpf, crm):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.crm = crm

    def __repr__(self):
        return f'<Medico {self.nome}>'

    

  