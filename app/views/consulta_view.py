from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.consulta_form import ConsultaForm
from app.models.consulta_model import Consulta
from app.models import prontuariopaciente_model, recepcionista_model, medico_model, planosaude_model

@app.route("/cadconsulta", methods=["POST", "GET"])
def cadastrar_consulta():
    form = ConsultaForm()

    
    prontuariospacientes = prontuariopaciente_model.ProntuarioPaciente.query.all()
    prontuario_escolhas = [(prontuario.id, prontuario.nome) for prontuario in prontuariospacientes]
    form.fk_prontuario_paciente.choices = prontuario_escolhas

    planos_saude = planosaude_model.PlanoSaude.query.all()
    plano_escolhas = [(plano.id, plano.nome) for plano in planos_saude]
    form.fk_plano_de_saude_id.choices = plano_escolhas
    
    medicos = medico_model.Medico.query.all()
    medico_escolhas = [(medico.id, medico.nome) for medico in medicos]
    form.fk_medico_id.choices = medico_escolhas
    
    recepcionistas = recepcionista_model.Recepcionista.query.all()
    recepcionista_escolhas = [(recepcionista.id, recepcionista.nome) for recepcionista in recepcionistas]
    form.fk_recepcionista_id.choices = recepcionista_escolhas
    
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
            db.session.rollback()
            flash(f"Erro ao cadastrar consulta: {e}", "danger")

    return render_template("consulta/consulta.html", form=form)


@app.route("/removerconsulta/<int:id>", methods=["GET", "POST"])
def remover_consulta(id):
    consulta_remover = Consulta.query.get_or_404(id)

    try:
        db.session.delete(consulta_remover)
        db.session.commit()
        flash("Consulta removida com sucesso!", "success")
    except Exception as e:
        print("Erro ao remover consulta:", e)
        db.session.rollback()
        flash("Erro ao remover consulta. Por favor, tente novamente mais tarde.", "error")

    return redirect(url_for('ver_consultas'))
