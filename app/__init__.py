from flask import Flask

from .models import User, Transaction, Budget, AIInsight  # Import models
from .blueprints import register_blueprints

from .extensions import db, migrate, bcrypt, jwt

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    register_blueprints(app)

    return app
