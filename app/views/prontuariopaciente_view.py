from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.prontuariopaciente_form import ProntuarioPacienteForm
from app.models.prontuariopaciente_model import ProntuarioPaciente

@app.route("/cadprontuario", methods=["POST", "GET"])
def cadastrar_prontuario():
    form = ProntuarioPacienteForm()
    if form.validate_on_submit():
        historico = form.historico.data
        whatsapp = form.whatsapp.data
        nome = form.nome.data
        email = form.email.data

        prontuario = ProntuarioPaciente(historico=historico, whatsapp=whatsapp, nome=nome, email=email)

        try:
            db.session.add(prontuario)
            db.session.commit()
            flash("Prontuário cadastrado com sucesso!", "success")
            return redirect(url_for('ver_prontuarios'))
        except Exception as e:
            db.session.rollback()
            flash("Erro ao cadastrar prontuário: " + str(e), "danger")

    return render_template('prontuariopaciente/prontuariopaciente.html', form=form)

@app.route("/verprontuarios")
def ver_prontuarios():
    prontuarios = ProntuarioPaciente.query.all()
    return render_template("prontuariopaciente/verprontuarios.html", prontuarios=prontuarios)

@app.route("/verumaprontuario/<int:id>")
def ver_um_prontuario(id):
    prontuario = ProntuarioPaciente.query.get_or_404(id)
    return render_template("prontuariopaciente/verumprontuario.html", prontuario=prontuario)

@app.route("/editarprontuario/<int:id>", methods=["GET", "POST"])
def editar_prontuario(id):
    prontuario_editar = ProntuarioPaciente.query.get_or_404(id)
    form = ProntuarioPacienteForm(obj=prontuario_editar)

    if form.validate_on_submit():
        prontuario_editar.historico = form.historico.data
        prontuario_editar.whatsapp = form.whatsapp.data
        prontuario_editar.nome = form.nome.data
        prontuario_editar.email = form.email.data
        try:
            db.session.commit()
            flash("Prontuário atualizado com sucesso!", "success")
            return redirect(url_for('ver_prontuarios'))
        except Exception as e:
            print("Erro ao atualizar prontuário:", e)
            db.session.rollback()
            flash("Erro ao atualizar prontuário. Por favor, tente novamente mais tarde.", "danger")

    return render_template("prontuariopaciente/prontuariopaciente.html", form=form, editar=True, prontuario_editar=prontuario_editar)


@app.route("/removerprontuario/<int:id>", methods=["GET", "POST"])
def remover_prontuario(id):
    prontuario_remover = ProntuarioPaciente.query.get_or_404(id)

    try:
        db.session.delete(prontuario_remover)
        db.session.commit()
        flash("Prontuário removido com sucesso!", "success")
    except Exception as e:
        print("Erro ao remover prontuário:", e)
        db.session.rollback()
        flash("Erro ao remover prontuário. Por favor, tente novamente mais tarde.", "danger")

    return redirect(url_for('ver_prontuarios'))
