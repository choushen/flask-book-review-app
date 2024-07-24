from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

#create the application object
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
admin = Admin(app)


from app import views, models
