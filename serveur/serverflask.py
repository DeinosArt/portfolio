from flask import Flask
import serveur.controllers as controllers



def start_serveur():
    app = Flask(__name__)
    controllers.register_routes(app)
    app.run(debug=True)