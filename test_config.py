from app.config import Config

print("Database URL:", Config.SQLALCHEMY_DATABASE_URI)
print("Secret Key:", Config.SECRET_KEY)
