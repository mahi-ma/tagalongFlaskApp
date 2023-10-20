from flask import Flask
from flask_login import LoginManager

app = Flask(__name)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)