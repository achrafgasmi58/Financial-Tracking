from flask import Blueprint
from app.extensions import db
from sqlalchemy import text


home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return "Welcome to the Financial Management App!"


