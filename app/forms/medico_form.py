from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MedicoForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    crm = StringField("crm", validators=[DataRequired()])


