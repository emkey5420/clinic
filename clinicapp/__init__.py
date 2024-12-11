from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)

app.secret_key = 'HGHJAHA^&^&*AJAVAHJ*^&^&*%&*^GAFGFAG'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/clinicdb?charset=utf8mb4" % quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)
login = LoginManager(app)

cloudinary.config(
    cloud_name="dahmfjhys",
    api_key="622554818371836",
    api_secret="BmTz1gn5IROBH8-uB72CnqLuAB4",  # Click 'View API Keys' above to copy your API secret
    secure=True
)
