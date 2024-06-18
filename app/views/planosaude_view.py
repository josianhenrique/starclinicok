# views/planosaude_view.py

from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.planodesaude_form import PlanoSaudeForm
from app.models.planosaude_model import PlanoSaude

@app.route("/planosaude", methods=["GET"])
def listar_planos():
    planos = PlanoSaude.query.all()
    return render_template("planosaude/listar_planos.html", planos=planos)

@app.route("/planosaude/<int:id>", methods=["GET"])
def ver_plano(id):
    plano = PlanoSaude.query.get_or_404(id)
    return render_template("planosaude/ver_plano.html", plano=plano)

@app.route("/planosaude/cadastrar", methods=["GET", "POST"])
def cadastrar_plano():
    form = PlanoSaudeForm()
    if form.validate_on_submit():
        nome = form.nome.data
        plano = PlanoSaude(nome=nome)
        try:
            db.session.add(plano)
            db.session.commit()
            flash("Plano de Saúde cadastrado com sucesso!", "success")
            return redirect(url_for('listar_planos'))
        except Exception as e:
            print("Erro ao cadastrar plano de saúde:", e)
            db.session.rollback()
            flash("Erro ao cadastrar plano de saúde. Por favor, tente novamente mais tarde.", "error")

    return render_template("planosaude/cadastrar_plano.html", form=form)

@app.route("/planosaude/editar/<int:id>", methods=["GET", "POST"])
def editar_plano(id):
    plano = PlanoSaude.query.get_or_404(id)
    form = PlanoSaudeForm(obj=plano)
    if form.validate_on_submit():
        plano.nome = form.nome.data
        try:
            db.session.commit()
            flash("Plano de Saúde atualizado com sucesso!", "success")
            return redirect(url_for('listar_planos'))
        except Exception as e:
            print("Erro ao atualizar plano de saúde:", e)
            db.session.rollback()
            flash("Erro ao atualizar plano de saúde. Por favor, tente novamente mais tarde.", "error")

    return render_template("planosaude/editar_plano.html", form=form, plano=plano)

@app.route("/planosaude/excluir/<int:id>", methods=["POST"])
def excluir_plano(id):
    plano = PlanoSaude.query.get_or_404(id)
    try:
        db.session.delete(plano)
        db.session.commit()
        flash("Plano de Saúde excluído com sucesso!", "success")
    except Exception as e:
        print("Erro ao excluir plano de saúde:", e)
        db.session.rollback()
        flash("Erro ao excluir plano de saúde. Por favor, tente novamente mais tarde.", "error")

    return redirect(url_for('listar_planos'))
