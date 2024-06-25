from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.models.especialidade_model import Especialidade

class MedicoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    crm = StringField('CRM', validators=[DataRequired()])
    especialidade_id = SelectField('Especialidade', coerce=int, choices=[])  # Adicione um valor padrão para choices
    submit = SubmitField('Cadastrar')

    def populate_especialidades(self):
        self.especialidade_id.choices = [(e.id, e.nome) for e in Especialidade.query.all()]
        if not self.especialidade_id.choices:  # Adicione uma escolha padrão se não houver especialidades
            self.especialidade_id.choices = [('', 'Nenhuma especialidade disponível')]
