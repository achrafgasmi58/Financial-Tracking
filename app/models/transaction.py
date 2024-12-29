from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Ensure this matches the User model
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = relationship('User', backref='transactions')  # Establish relationship
