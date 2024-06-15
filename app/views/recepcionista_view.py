# views/recepcionista_views.py
from app import app
from flask import render_template, redirect, url_for, flash
from app.forms.recepcionista_form import RecepcionistaForm
from app.models.recepcionista import Recepcionista
from app import db

@app.route("/cadrecepcionista", methods=["POST", "GET"])
def cadastrar_recepcionista():
    form = RecepcionistaForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        telefone = form.telefone.data
        senha = form.senha.data
        
        recepcionista = Recepcionista(nome=nome, email=email, telefone=telefone, senha=senha)
        
        try:
            db.session.add(recepcionista)
            db.session.commit()
            flash("Recepcionista cadastrado com sucesso!", "success")
            return redirect(url_for('cadastrar_recepcionista'))
        except Exception as e:
            db.session.rollback()
            flash("Erro ao cadastrar recepcionista: " + str(e), "danger")
    
    return render_template("recepcionista/form.html", form=form)
