from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize database and application
app = Flask(__name__, instance_relative_config=True, template_folder='templates')
app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app)