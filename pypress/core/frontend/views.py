from flask import Blueprint, render_template, url_for, redirect, abort, flash, request
from flask_login.utils import login_required, current_user
from sqlalchemy.exc import IntegrityError

from pypress.models import Post, db, User

frontend_blueprint = Blueprint('frontend', __name__, template_folder='../../templates/themes/default',
                               static_folder='../../templates/themes/default/static', static_url_path='/static/frontend')


@frontend_blueprint.route('/')
def front_index():
    return render_template('frontend_index.html')


@frontend_blueprint.route('/posts')
def front_posts():
    return 'Posts'


@frontend_blueprint.route('/posts/<slug>')
def front_post_view(slug):

    posts = []
    session = db.session()

    result = session.query(Post, User).filter_by(slug = slug).join(User, Post.user_id == User.id).first()

    print(result[0].slug)

    session.close()
    return result[0].content
