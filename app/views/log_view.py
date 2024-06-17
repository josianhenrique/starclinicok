from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.log_form import LogForm
from app.models.log import Log

@app.route("/cadlog", methods=["POST", "GET"])
def cadastrar_log():
    form = LogForm()
    if form.validate_on_submit():
        log = Log(
            hora=form.hora.data,
            hash_log=form.hash_log.data
        )
        try:
            db.session.add(log)
            db.session.commit()
            flash("Log cadastrado com sucesso!", "success")
            return redirect(url_for('cadastrar_log'))
        except Exception as e:
            print("Erro ao cadastrar log:", e)
            db.session.rollback()
            flash("Erro ao cadastrar log. Por favor, tente novamente mais tarde.", "error")
    
    return render_template("log/cadastrar_log.html", form=form)
