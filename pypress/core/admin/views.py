from flask import Blueprint, render_template, url_for, redirect, Markup, abort, flash, request
from flask_login.utils import login_required, current_user

from pypress.models import Post, User, db
from sqlalchemy.exc import IntegrityError

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


@admin_blueprint.get('/admin/posts/compose')
@login_required
def post_compose():
    return render_template('admin_ui.html', page='compose', title='Create a new post', file='compose.html')


@admin_blueprint.post('/admin/posts/compose')
@login_required
def post_compose_next():
    data = request.form

    post_content = data['editor1']
    title = data['title']
    meta_description = data['meta_description']
    slug = data['slug']
    tags = data['tags']
    category = data['category']
    no_index = 'off'

    try:
        no_index = data['no_index']
    except KeyError:
        pass

    try:
        post = Post(title, post_content, meta_description, slug, tags, category, no_index, current_user.id)
        print(post.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('admin.admin_posts'))
    except IntegrityError:
        flash('error')

    return render_template('admin_ui.html', page='compose', title='Create a new post', file='compose.html')
