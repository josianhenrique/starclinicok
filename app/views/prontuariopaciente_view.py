from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.prontuariopaciente_form import ProntuarioPacienteForm
from app.models.prontuariopaciente import ProntuarioPaciente  # Verifique o caminho correto aqui

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
            return redirect(url_for('cadastrar_prontuario'))
        except Exception as e:
            db.session.rollback()
            flash("Erro ao cadastrar prontuário: " + str(e), "danger")

    return render_template('prontuariopaciente/prontuariopaciente.html', form=form)
