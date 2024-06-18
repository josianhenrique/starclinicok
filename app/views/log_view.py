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

@app.route("/verlogs")
def ver_logs():
    logs = Log.query.all()
    return render_template("log/ver_logs.html", logs=logs)

@app.route("/verumlog/<int:id>")
def ver_um_log(id):
    log = Log.query.get_or_404(id)
    return render_template("log/ver_um_log.html", log=log)

@app.route("/editarlog/<int:id>", methods=["GET", "POST"])
def editar_log(id):
    log_editar = Log.query.get_or_404(id)
    form = LogForm(obj=log_editar)

    if form.validate_on_submit():
        log_editar.hora = form.hora.data
        log_editar.hash_log = form.hash_log.data
        try:
            db.session.commit()
            flash("Log atualizado com sucesso!", "success")
            return redirect(url_for('ver_logs'))
        except Exception as e:
            print("Erro ao atualizar log:", e)
            db.session.rollback()
            flash("Erro ao atualizar log. Por favor, tente novamente mais tarde.", "error")

    return render_template("log/cadastrar_log.html", form=form, editar=True)

@app.route("/removerlog/<int:id>", methods=["GET", "POST"])
def remover_log(id):
    log_remover = Log.query.get_or_404(id)

    try:
        db.session.delete(log_remover)
        db.session.commit()
        flash("Log removido com sucesso!", "success")
    except Exception as e:
        print("Erro ao remover log:", e)
        db.session.rollback()
        flash("Erro ao remover log. Por favor, tente novamente mais tarde.", "error")

    return redirect(url_for('ver_logs'))
