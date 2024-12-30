from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Budget(db.Model):
    __tablename__ = 'budget'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Ensure this matches the User model
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    user = relationship('User', backref='budgets')  # Establish relationship
