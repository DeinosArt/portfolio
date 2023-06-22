from flask import redirect, url_for

def register_route(app):
    @app.route("/")
    def hello_world():
        return redirect(url_for('portfolio'))
