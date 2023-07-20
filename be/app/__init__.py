import os

from app.config import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
enviroment = config["development"]
app.config.from_object(enviroment)
db = SQLAlchemy(app)

Migrate(app, db)