from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import especialidade_form
from app.models import especialidade
from app import db

@app.route("/cadespecial", methods=["POST", "GET"])
def cadastrar_especialidade():
    form = especialidade_form.EspecialidadeForm()
    if form.validate_on_submit():
        nome = form.nome.data
        especial = especialidade.Especialidade(nome=nome)
        try:
            db.session.add(especial)
            db.session.commit()
            flash("Especialidade cadastrada com sucesso!", "success")
            return redirect(url_for('ver_especialidades'))
        except Exception as e:
            print("Erro ao cadastrar especialidade:", e)
            db.session.rollback()
            flash("Erro ao cadastrar especialidade. Por favor, tente novamente mais tarde.", "error")

    return render_template("especialidade/especialidade.html", form=form)

@app.route("/verespecialidades")
def ver_especialidades():
    especialidades = especialidade.Especialidade.query.all()
    return render_template("especialidade/verespecialidades.html", especialidades=especialidades)
