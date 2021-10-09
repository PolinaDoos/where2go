from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

from webapp.config import Config

db = SQLAlchemy()  # creating db instance
app = Flask(__name__)
migrate = Migrate()
app.config.from_object(Config)

db.init_app(app)  #  bounding app and bd
migrate.init_app(app, db)  # bounfing app, bd and migration instance

from webapp import routes, model
