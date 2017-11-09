# manage.py

import os

from flask_migrate import Migrate
from flask_script import Manager

from web.app import db, create_app

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)