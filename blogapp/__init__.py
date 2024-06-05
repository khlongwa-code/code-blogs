from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "db.sqlite"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .models import User, Post

    create_database(app)


def create_database(app):
    with app.app_context():
        if not path.exists("blogapp/" + DB_NAME):
            db.create_all()
            print("Created database!")