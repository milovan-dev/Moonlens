from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

#Initialize extensions globally without binding to the app yet
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Initialize extensions with the app instance
    db.init_app(app)
    login_manager.init_app(app)
    
    #Configure authentication redirect
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # Import models so SQLAlchemy recognizes the database tables
    from app import models

    return app