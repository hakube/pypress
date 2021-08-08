
from flask import Blueprint


auth_page = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_page.route('/auth')
def auth():
    return 'Auth page'