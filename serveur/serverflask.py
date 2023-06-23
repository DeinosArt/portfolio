from flask import Flask
from flask_cors import CORS

import serveur.controllers as controllers



def start_serveur():
    app = Flask(__name__)
    CORS(app)
    controllers.register_routes(app)
    app.run(debug=True)