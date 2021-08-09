
from flask import Blueprint


auth_page = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_page.route('/login')
def auth():
    return 'Auth page for users'


@auth_page.route('/admin/login')
def auth_admin():
    return 'Auth page for administrators'