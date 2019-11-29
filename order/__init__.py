from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from order.config import DevConfig

app = Flask(__name__)

# load config from config.py
app.config.from_object(DevConfig)

# database object, defined in order.db.schema
db = SQLAlchemy(app)

import order.views

if __name__ == '__main__':
    app.run()