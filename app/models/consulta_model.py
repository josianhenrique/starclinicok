from sqlalchemy import Time, DateTime
from app import db
from sqlalchemy.orm import relationship

class Consulta(db.Model):  
    __tablename__ = "consulta"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.Float)
    data = db.Column(DateTime, nullable=False)
    horario = db.Column(Time)
    fk_recepcionista_id = db.Column(db.Integer, db.ForeignKey('recepcionista.id'))
    fk_medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    fk_prontuario_paciente = db.Column(db.Integer, db.ForeignKey('prontuario_paciente.id'))
    fk_plano_de_saude_id = db.Column(db.Integer, db.ForeignKey('plano_de_saude.id'))
    plano_de_saude = relationship("PlanoSaude", back_populates="consultas")

    def __repr__(self):
        return f'<Consulta {self.id} - {self.data}>'
