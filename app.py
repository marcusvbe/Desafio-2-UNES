from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route("/") # criando rotas com decorator
def index():
    return render_template("index.html")

@app.route("/contato.html")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos.html")
def quem_somos():
    return render_template("quemsomos.html")





