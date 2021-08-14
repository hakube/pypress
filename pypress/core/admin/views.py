from flask import Blueprint, render_template, url_for, redirect, Markup, abort, flash
from flask_login.utils import login_required


admin_blueprint = Blueprint('admin', __name__, template_folder='templates', static_folder='static')



@admin_blueprint.get('/admin')
@login_required
def admin():
    return render_template('admin_ui.html', page='admin', title='Dashboard', file='dashboard.html')

@admin_blueprint.get('/admin/posts')
@login_required
def admin_posts():
    return render_template('admin_ui.html', page='posts', title='Posts', file='posts.html')

@admin_blueprint.get('/admin/pages')
@login_required
def admin_pages():
    return render_template('admin_ui.html', page='pages', title='Pages', file='pages.html')

@admin_blueprint.get('/admin/comments')
@login_required
def admin_comments():
    return render_template('admin_ui.html', page='comments', title='Comments', file='comments.html')


@admin_blueprint.get('/admin/users')
@login_required
def admin_users():
    return render_template('admin_ui.html', page='users', title='Users', file='users.html')


@admin_blueprint.get('/admin/settings')
@login_required
def admin_settings():
    return render_template('admin_ui.html', page='settings', title='Settings', file='settings.html')


@admin_blueprint.route('/admin/posts/compose')
@login_required
def post_compose():
    return render_template('admin_ui.html', page='compose', title='Create a new post', file='compose.html')