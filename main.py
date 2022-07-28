from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db, create_app, models

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/create_all')
def create_all():
    db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
    return 'Criado com sucesso!!'
