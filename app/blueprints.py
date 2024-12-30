from flask import Flask
from .routes.transaction import transaction_bp
from .routes.budget import budget_bp
from .routes.home import home_bp  # Import the home blueprint
from .routes.auth import auth_bp  # Import the auth blueprint

def register_blueprints(app: Flask):
    app.register_blueprint(home_bp, url_prefix='/')  # Default route
    app.register_blueprint(transaction_bp, url_prefix='/transactions')
    app.register_blueprint(budget_bp, url_prefix='/budgets')
    app.register_blueprint(auth_bp, url_prefix='/auth')
