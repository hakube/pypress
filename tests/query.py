from pypress.models import Post, User, db
from pypress import app


with app.app_context() as afp:

    session = db.session()

    result = session.query(Post.id, Post.title, User.name, Post.date_posted)

    for q in result:
        print(q)
    session.close()