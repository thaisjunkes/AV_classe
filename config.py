from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'saude.db')
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
