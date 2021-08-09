
from flask import Blueprint, render_template

from . import posts

admin_page = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
admin_page.register_blueprint(posts.posts_page)



@admin_page.route('/admin')
def admin():
    return render_template('admin_ui.html', page='admin', title='Dashboard', file='dashboard.html')

@admin_page.route('/admin/posts')
def admin_posts():
    return render_template('admin_ui.html', page='posts', title='Posts', file='posts.html')

@admin_page.route('/admin/pages')
def admin_pages():
    return render_template('admin_ui.html', page='pages', title='Pages', file='pages.html')

@admin_page.route('/admin/comments')
def admin_comments():
    return render_template('admin_ui.html', page='comments', title='Comments', file='comments.html')


@admin_page.route('/admin/users')
def admin_users():
    return render_template('admin_ui.html', page='users', title='Users', file='users.html')


@admin_page.route('/admin/settings')
def admin_settings():
    return render_template('admin_ui.html', page='settings', title='Settings', file='settings.html')