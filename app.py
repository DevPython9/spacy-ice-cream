from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return “<p>Ceci est le début de l’aventure de Spacy Ice-Cream!</p>”