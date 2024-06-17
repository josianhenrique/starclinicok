from flask import render_template, redirect, url_for
from app import app, db
from app.forms import planodesaude_form
from app.models import planosaude_model

@app.route("/cadplanosaude", methods=["POST", "GET"])
def cadastrar_planosaude():
    form = planodesaude_form.PlanoSaudeForm()
    if form.validate_on_submit():
        nome = form.nome.data
        planosaude = planosaude_model.PlanoSaude(nome=nome)
        try:
            db.session.add(planosaude)
            db.session.commit()
            return redirect(url_for('sucesso'))  # Redireciona para uma página de sucesso
        except Exception as e:
            print("Erro ao cadastrar plano de saúde:", e)
            db.session.rollback()  # Desfaz qualquer alteração na sessão em caso de erro
            return "Erro ao cadastrar plano de saúde. Por favor, tente novamente mais tarde."

    return render_template("planosaude/planosaude.html", form=form)



