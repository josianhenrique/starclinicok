from app import db
class PlanoSaude(db.Model):
    __tablename__ = "plano_de_saude"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(55), nullable=False)

    def __repr__(self):
        return f"<PlanoSaude {self.id} - {self.nome}>"
