# app/routes/planosaude_routes.py

from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.planosaude_form import PlanoSaudeForm
from app.models.planosaude_model import PlanoSaude

@app.route("/cadplanosaude", methods=["POST", "GET"])
def cadastrar_plano():
    form = PlanoSaudeForm()
    if form.validate_on_submit():
        nome = form.nome.data

        plano = PlanoSaude(nome=nome)

        try:
            db.session.add(plano)
            db.session.commit()
            flash("Plano de Saúde cadastrado com sucesso!", "success")
            return redirect(url_for('ver_planos'))
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao cadastrar plano de saúde: {str(e)}", "danger")

    return render_template('planosaude/cadplanosaude.html', form=form)

@app.route("/verplanos")
def ver_planos():
    planos = PlanoSaude.query.all()
    return render_template("planosaude/verplanosaude.html", planos=planos)

@app.route("/verumplanosaude/<int:id>")
def ver_um_plano(id):
    plano = PlanoSaude.query.get_or_404(id)
    return render_template("planosaude/verumplanosaude.html", plano=plano)

@app.route("/editarplanosaude/<int:id>", methods=["GET", "POST"])
def editar_plano(id):
    plano_editar = PlanoSaude.query.get_or_404(id)
    form = PlanoSaudeForm(obj=plano_editar)

    if form.validate_on_submit():
        plano_editar.nome = form.nome.data
        try:
            db.session.commit()
            flash("Plano de Saúde atualizado com sucesso!", "success")
            return redirect(url_for('ver_planos'))
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao atualizar plano de saúde: {str(e)}", "danger")

    return render_template("planosaude/editarplanosaude.html", form=form, plano_editar=plano_editar)

@app.route("/removerplanosaude/<int:id>", methods=["POST"])
def remover_plano(id):
    plano_remover = PlanoSaude.query.get_or_404(id)

    try:
        db.session.delete(plano_remover)
        db.session.commit()
        flash("Plano de Saúde removido com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao remover plano de saúde: {str(e)}", "danger")

    return redirect(url_for('ver_planos'))
