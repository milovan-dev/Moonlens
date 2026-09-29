# Standard library import for handling timestamps
from datetime import datetime
# Flask-Login mixin for default user implementation
from flask_login import UserMixin
# Password hashing utilities for secure authentication
from werkzeug.security import generate_password_hash, check_password_hash
# Import database and login manager instances from application package
from app import db, login_manager

# Flask-Login callback to load a user by ID from the database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User model representing admin users in the database
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Hashes the plain text password and stores it
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Verifies if the provided password matches the stored hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # String representation of the User object for debugging
    def __repr__(self):
        return f"<User {self.username}>"


class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Photo {self.title}>"