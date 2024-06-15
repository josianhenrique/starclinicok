from app import app
from flask import render_template, redirect, url_for, flash
from app.forms.medico_form import MedicoForm  # Certifique-se de importar corretamente o formulário
from app.models.medico import Medico  # Certifique-se de importar corretamente o modelo
from app import db

@app.route("/cadmedico", methods=["POST", "GET"])
def cadastrar_medico():
    form = MedicoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        telefone = form.telefone.data
        cpf = form.cpf.data
        crm = form.crm.data
        
        medico = Medico(nome=nome, telefone=telefone, cpf=cpf, crm=crm)
        
        try:
            db.session.add(medico)
            db.session.commit()
            flash("Médico cadastrado com sucesso!", "success")
            return redirect(url_for('cadastrar_medico'))
        except Exception as e:
            db.session.rollback()
            flash("Erro ao cadastrar médico: " + str(e), "danger")
    
    return render_template("medico/form.html", form=form)
