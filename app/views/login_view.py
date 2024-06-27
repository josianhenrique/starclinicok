from app import app
from flask import render_template, redirect, url_for, flash
from app import db

@app.route("/entrar", methods=["POST", "GET"])
def abrir_index():
   return render_template("login/login.html")