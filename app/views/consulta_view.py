from app import app
from flask import render_template, redirect, url_for, flash
from app.forms.consulta_form import ConsultaForm
from app.models.consulta import Consulta
from app import db
from app.models import prontuariopaciente_model


@app.route("/cadconsulta", methods=["POST", "GET"])
def cadastrar_consulta():
    form = ConsultaForm()
    prontuariospacientes = prontuariopaciente_model.ProntuarioPaciente.query.all()
    prontuario_escolhas = [(prontuariopaciente.id,prontuariopaciente.nome) for prontuariopaciente in prontuariospacientes]
    form.prontuario_paciente.id.escolhas = prontuario_escolhas
    if form.validate_on_submit():
        valor = form.valor.data
        data = form.data.data
        horario = form.horario.data
        fk_recepcionista_id = form.fk_recepcionista_id.data
        fk_medico_id = form.fk_medico_id.data
        fk_prontuario_paciente = form.fk_prontuario_paciente.data
        fk_plano_de_saude_id = form.fk_plano_de_saude_id.data

        consulta = Consulta(
            valor=valor,
            data=data,
            horario=horario,
            fk_recepcionista_id=fk_recepcionista_id,
            fk_medico_id=fk_medico_id,
            fk_prontuario_paciente=fk_prontuario_paciente,
            fk_plano_de_saude_id=fk_plano_de_saude_id
        )

        try:
            db.session.add(consulta)
            db.session.commit()
            flash("Consulta cadastrada com sucesso!", "success")
            return redirect(url_for('cadastrar_consulta'))
        except Exception as e:
            print("Erro ao cadastrar consulta:", e)
            db.session.rollback()
            flash("Erro ao cadastrar consulta. Por favor, tente novamente mais tarde.", "error")

    return render_template("consulta/consulta.html", form=form)
