from flask import jsonify
from flask_cors import cross_origin
import random
import serveur.models as models

def register_route(app):
    @app.route("/image")
    @cross_origin()
    def image():
        images = models.get_images()
        random_image = random.choice(images)
        return jsonify(random_image)
