from app import db
from sqlalchemy.orm import relationship

class PlanoSaude(db.Model):
    __tablename__ = "plano_de_saude"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    consultas = relationship("Consulta", back_populates="plano_de_saude")

    def __repr__(self):
        return f"<PlanoSaude {self.id} - {self.nome}>"
