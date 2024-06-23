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
            return redirect(url_for('ver_consultas'))
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao cadastrar consulta: {e}", "danger")

    return render_template("consulta/consulta.html", form=form)

@app.route('/consultas/<int:id>')
def ver_uma_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    return render_template('consulta/verumaconsulta.html', consulta=consulta)
   
@app.route("/removerconsulta/<int:id>", methods=["GET", "POST"])
def remover_consulta(id):
    consulta_remover = Consulta.query.get_or_404(id)

    try:
        db.session.delete(consulta_remover)
        db.session.commit()
        flash("Consulta removida com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao remover consulta: {e}", "danger")

    return redirect(url_for('ver_consultas'))

@app.route("/verconsultas")
def ver_consultas():
    consultas = Consulta.query.all()
    return render_template("consulta/verconsultas.html", consultas=consultas)

@app.route("/editarconsulta/<int:id>", methods=["GET", "POST"])
def editar_consulta(id):
    consulta_editar = Consulta.query.get_or_404(id)
    form = ConsultaForm(obj=consulta_editar)

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
        consulta_editar.valor = form.valor.data
        consulta_editar.data = form.data.data
        consulta_editar.horario = form.horario.data
        consulta_editar.recepcionista_id = form.recepcionista_id.data
        consulta_editar.medico_id = form.medico_id.data
        consulta_editar.prontuario_paciente_id = form.prontuario_paciente_id.data
        consulta_editar.plano_de_saude_id = form.plano_de_saude_id.data
        form.populate_obj(consulta_editar)

        try:
            db.session.commit()
            flash("Consulta atualizada com sucesso!", "success")
            return redirect(url_for('ver_consultas'))
        except Exception as e:
            print("Erro ao atualizar consulta:", e)
            db.session.rollback()
            flash("Erro ao atualizar consulta. Por favor, tente novamente mais tarde.", "danger")

    return render_template("consulta/consulta.html", form=form, editar=True, consulta_editar=consulta_editar)