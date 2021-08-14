
from flask_login.mixins import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

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

    def __init__(self,  email, name, password, role, salt, created_at, id=None):
        self.id = id
        self.email = email
        self.name = name
        self.password = password
        self.role = role
        self.salt = salt
        self.created_at = created_at

    def is_active(self): return True

    def get_id(self): return self.id

    def is_authenticated(self):
        return self.authenticated
    
        
