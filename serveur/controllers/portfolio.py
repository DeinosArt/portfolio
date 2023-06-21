from flask import render_template
import time
import serveur.models as models

def register_route(app):
    @app.route("/portfolio")
    def portfolio():
        images = models.get_images(True)
        return render_template(
            'portfolio.html', 
            TIME=time.time(),
            images=images
        )