import os

class Config:
    """Base configuration class for application settings."""
    
    # Secret key for signing session cookies and securing forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'moonlens-super-secret-key-12345'

    # Database connection string for MySQL via PyMySQL
    # Format: mysql+pymysql://username:password@localhost/database_name
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:@localhost/moonlens'

    # Disable track modifications to save memory and avoid overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False