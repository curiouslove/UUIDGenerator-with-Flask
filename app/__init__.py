from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///uuiddb.db'
db = SQLAlchemy(app)



from app import views
from app import models