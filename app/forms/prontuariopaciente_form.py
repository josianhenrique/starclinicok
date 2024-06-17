from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ProntuarioPacienteForm(FlaskForm):
    historico = StringField("Histórico", validators=[DataRequired()])
    nome = StringField("Nome", validators=[DataRequired()])
    whatsapp = StringField("WhatsApp", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
