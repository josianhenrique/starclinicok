# app/forms/consulta_form.py
from flask_wtf import FlaskForm
from wtforms import FloatField, DateTimeField, TimeField, IntegerField, SelectField
from wtforms.validators import DataRequired

class ConsultaForm(FlaskForm):
    valor = FloatField("Valor", validators=[DataRequired()])
    data = DateTimeField("Data", format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    horario = TimeField("Horario", format='%H:%M:%S', validators=[DataRequired()])
    fk_recepcionista_id = IntegerField("Recepcionista ID", validators=[DataRequired()])
    fk_medico_id = IntegerField("Medico ID", validators=[DataRequired()])
    fk_prontuario_paciente = SelectField("Prontuario Paciente", coerce=int, validators=[DataRequired()])
    fk_plano_de_saude_id = IntegerField("Plano de Saude ID", validators=[DataRequired()])
