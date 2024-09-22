from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from app.model.user import User

