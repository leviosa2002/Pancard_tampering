from flask import Flask
import os

app = Flask(__name__)

app.config["ENV"] = os.environ.get("FLASK_ENV", "production")

if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
