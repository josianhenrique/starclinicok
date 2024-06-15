from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import planodesaude_form
from app.models import planosaude_model
from app import db
@app.route("/cadplanosaude",methods=["POST","GET"])
def cadastrar_planosaude():
      form = planodesaude_form.PlanoSaudeForm()
      if form.validate_on_submit():
        nome = form.nome.data #capturando o conteúdo validado
        planosaude = planosaude_model.PlanoSaude(nome=nome)
        try:
          #adicionar na sessão 
           db.session.add(planosaude)
          #salvar a sessão
           db.session.commit()
          
        except:
         print("plano de saude não cadastrado")
      return render_template("planosaude/index.html",form=form)