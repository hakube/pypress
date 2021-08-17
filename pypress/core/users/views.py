from flask import Blueprint, render_template, request, url_for, redirect, flash, abort, Markup
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import exc
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash, gen_salt
from pypress.models import User, db
import time

users = Blueprint('users', __name__, template_folder='templates')


@users.get('/admin/register')
@login_required
def admin_register():
    return render_template('admin_auth_signup.html')


@users.post('/admin/register')
@login_required
def admin_register_next():
    if current_user.role not in ['admin'] and current_user.authenticate == False: redirect(url_for('index'))
    data = request.form

    email = data['email']
    password = data['password']
    password_confirmation = data['passwordc']
    name = data['name']
    role = data['role']

    user = User.query.filter_by(email=email).first()

    if user is None and password == password_confirmation:
        print(data)
        try:
            password = generate_password_hash(password)

            new_user = User(email, name, password, role, gen_salt(16), time.time())
            new_user.authenticated = True
            db.session.add(new_user)
            db.session.commit()
            message = Markup(
                "<strong>Success!</strong> Thanks for registering. Please check your email to confirm your email address.")
            flash(message, 'success')
            return redirect(url_for('users.login', success="true"))
        except IntegrityError:
            print('integrity error')
            db.session.rollback()
            message = Markup(
                "<strong>Error!</strong> Unable to process registration.")
            flash(message, 'danger')

    return render_template('admin_auth_signup.html')


@users.get('/login')
def login():
    return render_template('admin_auth.html')


@users.post('/login')
def login_next():
    data = request.form

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if email == user.email and check_password_hash(user.password, password):
        print("Verified user")
        login_user(user, remember=True)

        next = request.args.get('next')

        return redirect(next or url_for('index'))

    return render_template('admin_auth.html')


@users.get('/logout')
def logout():
    logout_user()
    next = request.args.get('next')
    return redirect(url_for(next or 'index'))
