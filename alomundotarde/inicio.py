print("alo mundo")
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/inicio")
def ola():
    return "ola mundo"

@app.route("/olamundo")
def mostrar():
    return render_template ('pagina.html')
app.run()
