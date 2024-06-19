# app/views.py
from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms.consulta_form import ConsultaForm
from app.models.consulta_model import Consulta
from app.models import prontuariopaciente_model

@app.route("/cadconsulta", methods=["POST", "GET"])
def cadastrar_consulta():
    form = ConsultaForm()
    
    # Obter prontuários de pacientes do banco de dados
    prontuariospacientes = prontuariopaciente_model.ProntuarioPaciente.query.all()
    prontuario_escolhas = [(prontuariopaciente.id, prontuariopaciente.nome) for prontuariopaciente in prontuariospacientes]
    form.fk_prontuario_paciente.choices = prontuario_escolhas
    
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

@app.route("/verconsultas")
def ver_consultas():
    consultas = Consulta.query.all()
    return render_template("consulta/verconsultas.html", consultas=consultas)

@app.route("/verumaconsulta/<int:id>")
def ver_uma_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    return render_template("consulta/verumaconsulta.html", consulta=consulta)

@app.route("/editarconsulta/<int:id>", methods=["GET", "POST"])
def editar_consulta(id):
    consulta_editar = Consulta.query.get_or_404(id)
    form = ConsultaForm(obj=consulta_editar)
    prontuariospacientes = prontuariopaciente_model.ProntuarioPaciente.query.all()
    prontuario_escolhas = [(prontuario.id, prontuario.nome) for prontuario in prontuariospacientes]
    form.fk_prontuario_paciente.choices = prontuario_escolhas

    if form.validate_on_submit():
        consulta_editar.valor = form.valor.data
        consulta_editar.data = form.data.data
        consulta_editar.horario = form.horario.data
        consulta_editar.fk_recepcionista_id = form.fk_recepcionista_id.data
        consulta_editar.fk_medico_id = form.fk_medico_id.data
        consulta_editar.fk_prontuario_paciente = form.fk_prontuario_paciente.data
        consulta_editar.fk_plano_de_saude_id = form.fk_plano_de_saude_id.data

        try:
            db.session.commit()
            flash("Consulta atualizada com sucesso!", "success")
            return redirect(url_for('ver_consultas'))
        except Exception as e:
            print("Erro ao atualizar consulta:", e)
            db.session.rollback()
            flash("Erro ao atualizar consulta. Por favor, tente novamente mais tarde.", "error")

    return render_template("consulta/consulta.html", form=form, editar=True)

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


