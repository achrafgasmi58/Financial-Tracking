from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class AIInsight(db.Model):
    __tablename__ = 'ai_insight'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Ensure 'users.id' matches the User model's table name
    insight = db.Column(db.Text, nullable=False)

    user = relationship('User', backref='ai_insights')  # Establish relationship
