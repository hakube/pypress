
from flask import Blueprint


admin_page = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

@admin_page.route('/admin')
def admin():
    return 'Admin page'