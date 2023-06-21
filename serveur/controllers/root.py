from flask import render_template

def register_route(app):
    @app.route("/")
    def hello_world():
        return render_template(
            'hello.html',
            name="jojo" 
        )
