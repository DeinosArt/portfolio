import serveur.controllers.root
import serveur.controllers.portfolio
import serveur.controllers.api.image


def register_routes(app):
    serveur.controllers.root.register_route(app)
    serveur.controllers.portfolio.register_route(app)
    serveur.controllers.api.image.register_route(app)
