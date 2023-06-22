from flask import Flask
import serveur.controllers as controllers

# global to run on https://help.pythonanywhere.com/pages/Flask/
app = Flask(__name__)
controllers.register_routes(app)

def start_serveur():
    app.run(debug=True)