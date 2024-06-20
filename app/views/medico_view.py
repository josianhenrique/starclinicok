from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.medico_form import MedicoForm
from app.models.medico_model import Medico

@app.route("/cadmedico", methods=["POST", "GET"])
def cadastrar_medico():
    form = MedicoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        telefone = form.telefone.data
        cpf = form.cpf.data
        crm = form.crm.data

        medico = Medico(nome=nome, telefone=telefone, cpf=cpf, crm=crm)

        try:
            db.session.add(medico)
            db.session.commit()
            flash("Médico cadastrado com sucesso!", "success")
            return redirect(url_for('ver_medicos'))
        except Exception as e:
            db.session.rollback()
            flash("Erro ao cadastrar médico: " + str(e), "danger")

    return render_template('medico/medico.html', form=form)

@app.route("/vermedicos")
def ver_medicos():
    medicos = Medico.query.all()
    return render_template("medico/vermedicos.html", medicos=medicos)

@app.route("/verumamedico/<int:id>")
def ver_um_medico(id):
    medico = Medico.query.get_or_404(id)
    return render_template("medico/verummedico.html", medico=medico)

@app.route("/editarmedico/<int:id>", methods=["GET", "POST"])
def editar_medico(id):
    medico_editar = Medico.query.get_or_404(id)
    form = MedicoForm(obj=medico_editar)

    if form.validate_on_submit():
        medico_editar.nome = form.nome.data
        medico_editar.telefone = form.telefone.data
        medico_editar.cpf = form.cpf.data
        medico_editar.crm = form.crm.data
        try:
            db.session.commit()
            flash("Médico atualizado com sucesso!", "success")
            return redirect(url_for('ver_medicos'))
        except Exception as e:
            db.session.rollback()
            flash("Erro ao atualizar médico. Por favor, tente novamente mais tarde.", "danger")

    return render_template("medico/medico.html", form=form, editar=True, medico_editar=medico_editar)

@app.route("/removermedico/<int:id>", methods=["GET", "POST"])
def remover_medico(id):
    medico_remover = Medico.query.get_or_404(id)

    try:
        db.session.delete(medico_remover)
        db.session.commit()
        flash("Médico removido com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Erro ao remover médico. Por favor, tente novamente mais tarde.", "danger")

    return redirect(url_for('ver_medicos'))
