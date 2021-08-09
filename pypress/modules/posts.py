from flask import Blueprint, render_template


posts_page = Blueprint('posts', __name__, template_folder='templates', static_folder='static')

@posts_page.route('/admin/posts/compose')
def post_compose():

    return render_template('admin_ui.html', page='compose', title='New post', file='compose.html')