from flask import Flask
from flask_cors import CORS
from uofg.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    from uofg.api.routes import api

    app.register_blueprint(api)

    return app