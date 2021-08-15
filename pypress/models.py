from flask_login.mixins import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.String(255), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    role = db.Column(db.String(30), unique=False, nullable=False)
    salt = db.Column(db.String(255), unique=False, nullable=False)
    created_at = db.Column(db.Float(), unique=False, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, email, name, password, role, salt, created_at, id=None):
        self.id = id
        self.email = email
        self.name = name
        self.password = password
        self.role = role
        self.salt = salt
        self.created_at = created_at

    def is_active(self): return True

    def get_id(self): return self.id


class Post(db.Model):
    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)
    meta_description = db.Column(db.Text(), nullable=True)
    slug = db.Column(db.String(100), nullable=True)
    tags = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    no_index = db.Column(db.String(3), nullable=True, default='off')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, title, content, meta_description, slug, tags, category, noindex, author):

        self.title = title
        self.content = content
        self.meta_description = meta_description
        self.slug = slug
        self.tags = tags
        self.category = category
        self.no_index = noindex
        self.user_id = author
