from flask import Flask
from sqlalchemy import text

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

    # Test database connection route (for development only)
    # @app.route('/test-db', methods=['GET'])
    # def test_db():
    #     try:
    #         db.session.execute(text('SELECT 1'))  # Use text() for raw SQL
    #         return "Database connection successful!", 200
    #     except Exception as e:
    #         return f"Database connection failed: {str(e)}", 500

    return app
