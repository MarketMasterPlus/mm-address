# mm-address/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

db = SQLAlchemy()  # Ensure a single instance of SQLAlchemy
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv()

    # Load database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'postgresql://marketmaster:password@db:5432/marketmaster'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy instance with the Flask app
    db.init_app(app)
    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    # Register the blueprint for the API
    from .api.routes import blueprint as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
