from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.recepcionista_form import RecepcionistaForm
from app.models.recepcionista_model import Recepcionista

@app.route("/cadrecepcionista", methods=["GET", "POST"])
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
            return redirect(url_for('ver_recepcionistas'))
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao cadastrar recepcionista: {str(e)}", "danger")

    return render_template('recepcionista/recepcionista.html', form=form)

@app.route("/verrecepcionistas")
def ver_recepcionistas():
    recepcionistas = Recepcionista.query.all()
    return render_template("recepcionista/verrecepcionistas.html", recepcionistas=recepcionistas)

@app.route("/verumrecepcionista/<int:id>")
def ver_um_recepcionista(id):
    recepcionista = Recepcionista.query.get_or_404(id)
    return render_template("recepcionista/verumrecepcionista.html", recepcionista=recepcionista)



@app.route("/editarrecepcionista/<int:id>", methods=["GET", "POST"])
def editar_recepcionista(id):
    recepcionista_editar = Recepcionista.query.get_or_404(id)
    form = RecepcionistaForm(obj=recepcionista_editar)

    if form.validate_on_submit():
        form.populate_obj(recepcionista_editar)
        try:
            db.session.commit()
            flash("Recepcionista atualizado com sucesso!", "success")
            return redirect(url_for('ver_recepcionistas'))
        except Exception as e:
            print("Erro ao atualizar recepcionista:", e)
            db.session.rollback()
            flash("Erro ao atualizar recepcionista. Por favor, tente novamente mais tarde.", "danger")

    return render_template("recepcionista/recepcionista.html", form=form, editar=True, recepcionista=recepcionista_editar)
    
@app.route("/removerrecepcionista/<int:id>", methods=["GET", "POST"])
def remover_recepcionista(id):
    recepcionista_remover = Recepcionista.query.get_or_404(id)

    try:
        db.session.delete(recepcionista_remover)
        db.session.commit()
        flash("Recepcionista removido com sucesso!", "success")
    except Exception as e:
        print("Erro ao remover recepcionista:", e)
        db.session.rollback()
        flash("Erro ao remover recepcionista. Por favor, tente novamente mais tarde.", "danger")

    return redirect(url_for('ver_recepcionistas'))
