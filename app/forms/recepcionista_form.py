from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RecepcionistaForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])