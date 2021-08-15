from flask.templating import render_template
from .core.users.views import users
from .core.admin.views import admin_blueprint
from flask import Flask
from .models import db, User
from flask_login.login_manager import LoginManager
from flask_login import login_required
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.secret_key = 'This is the secret'

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = "users.login"

db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)

with app.app_context():
    db.create_all()


# Initialize user loader

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


# Initialize blueprints
app.register_blueprint(users)
app.register_blueprint(admin_blueprint)


# routes
@app.get('/')
@login_required
def index():
    return render_template('index.html')
