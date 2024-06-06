import datetime
from sqlalchemy import Time, DateTime
from app import db
class Consulta(db.Model):  
    __tablename__ = "consulta"
    horario = db.Column(Time)
    data = db.Column(DateTime, nullable=False)

    idConsulta = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fk_recepcionista_id = db.Column(db.Integer,db.ForeignKey('recepcionista.id'))
    fk_medico_id = db.Column(db.Integer,db.ForeignKey('medico.id'))
    fk_paciente_id = db.Column(db.Integer,db.ForeignKey('paciente.id'))