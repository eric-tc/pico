# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('profile.html', name=current_user.name)
    else:

        return render_template('login.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)