from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class MedicoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    telefone = StringField("Telefone", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired()])
    crm = StringField("CRM", validators=[DataRequired()])
    especialidade_id = SelectField('Especialidade', coerce=int, validators=[DataRequired()])
    


