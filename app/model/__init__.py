# app/__init__.py

from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config

# Local import


# Initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
