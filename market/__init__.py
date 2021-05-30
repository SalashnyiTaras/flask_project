from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from market.extensions import csrf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'f97ce75c6bf54bd873fc1fc6'
db = SQLAlchemy(app)


# When debug is on, changes in the code are displaying in web server immediately, no need to restart
# Do not forget to turn off debug in production
from market import routes
