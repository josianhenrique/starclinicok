from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class ConsultaForm(FlaskForm):
    valor = FloatField("Valor", validators=[DataRequired()])
    data = DateField("Data", validators=[DataRequired()])
    horario = TimeField("Horário", validators=[DataRequired()])
    fk_recepcionista_id = SelectField("Recepcionista", coerce=int, validators=[DataRequired()])
    fk_medico_id = SelectField("Médico", coerce=int, validators=[DataRequired()])
    fk_prontuario_paciente = SelectField("Prontuário do Paciente", coerce=int, validators=[DataRequired()])
    fk_plano_de_saude_id = SelectField("Plano de Saúde", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Salvar")
