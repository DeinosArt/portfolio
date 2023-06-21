import serveur.controllers.root
import serveur.controllers.portfolio


def register_routes(app):
    serveur.controllers.root.register_route(app)
    serveur.controllers.portfolio.register_route(app)
