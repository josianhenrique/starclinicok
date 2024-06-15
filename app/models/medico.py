from app import db
class Medico(db.Model):  
    __tablename__ = "medico"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(80))
    telefone = db.Column(db.String(12))
    codigo_acesso = db.Column(db.Integer)
    cpf = db.Column(db.String(12))
    crm = db.Column(db.String(60))
    fk_especialidade_id= db.Column(db.Integer,db.ForeignKey('especialidade.id'))
    

  