from flask import Flask

#Routes
from src.main.routes.trips_routes import trips_routes_bp
from src.main.routes.link_routes import links_routes_bp

app = Flask(__name__)

app.register_blueprint(trips_routes_bp)
app.register_blueprint(links_routes_bp)