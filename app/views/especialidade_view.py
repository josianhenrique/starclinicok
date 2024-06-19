from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import especialidade_form
from app.models import especialidade_model

@app.route("/cadespecial", methods=["POST", "GET"])
def cadastrar_especialidade():
    form = especialidade_form.EspecialidadeForm()
    if form.validate_on_submit():
        nome = form.nome.data
        especial = especialidade_model.Especialidade(nome=nome)
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
    especialidades = especialidade_model.Especialidade.query.all()
    return render_template("especialidade/verespecialidades.html", especialidades=especialidades)

@app.route("/verumaespecial/<int:id>")
def ver_uma_especial(id):
    especial = especialidade_model.Especialidade.query.filter_by(id=id).first()
    return render_template("especialidade/verumaespecialidade.html", especial=especial)

@app.route("/editarespecialidade/<int:id>", methods=["GET", "POST"])
def editar_especialidade(id):
    especialidade_editar = especialidade_model.Especialidade.query.get_or_404(id)
    form = especialidade_form.EspecialidadeForm(obj=especialidade_editar)

    if form.validate_on_submit():
        especialidade_editar.nome = form.nome.data
        try:
            db.session.commit()
            flash("Especialidade atualizada com sucesso!", "success")
            return redirect(url_for('ver_especialidades'))
        except Exception as e:
            print("Erro ao atualizar especialidade:", e)
            db.session.rollback()
            flash("Erro ao atualizar especialidade. Por favor, tente novamente mais tarde.", "error")

    return render_template("especialidade/especialidade.html", form=form, editar=True)

@app.route("/removerespecialidade/<int:id>", methods=["GET", "POST"])
def remover_especialidade(id):
    especialidade_remover = especialidade_model.Especialidade.query.get_or_404(id)

    try:
        db.session.delete(especialidade_remover)
        db.session.commit()
        flash("Especialidade removida com sucesso!", "success")
    except Exception as e:
        print("Erro ao remover especialidade:", e)
        db.session.rollback()
        flash("Erro ao remover especialidade. Por favor, tente novamente mais tarde.", "error")

    return redirect(url_for('ver_especialidades'))
