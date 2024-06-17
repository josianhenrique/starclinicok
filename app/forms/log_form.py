from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired

class LogForm(FlaskForm):
    hora = DateTimeField("Hora", format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    hash_log = StringField("Hash Log", validators=[DataRequired()])
