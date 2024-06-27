
from app import app
from flask import render_template, redirect, url_for, flash


@app.route("/", methods=["GET", "POST"])
def site():
    
    return render_template("site/index.html")