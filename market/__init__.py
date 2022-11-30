from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ceeab11e0b9cae1493a765a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db=SQLAlchemy(app)



from market import routes
