from flask import Flask
from uofg.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from uofg.api.routes import api

    app.register_blueprint(api)

    return app