from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import StringField
from wtforms.validators import DataRequired


class ProntuarioPacienteForm(FlaskForm):
    historico = TextAreaField("Histórico", validators=[DataRequired()])
    nome = StringField("Nome", validators=[DataRequired()])
    whatsapp = StringField("WhatsApp", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
