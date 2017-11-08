# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from {{cookiecutter.app_name}}.extensions import bcrypt, db


class Role(db.Document):
    """A role for a user."""

    __tablename__ = 'roles'
    name = db.StringField(max_length=100, unique=True, required=True)



class User(UserMixin, db.Document):
    """A user of the app."""

    __tablename__ = 'users'
    username = db.StringField(150, unique=True, required=True)
    email = db.StringField(150, unique=True, required=True)
    password = db.BinaryField(128, required=True)
    created_at = db.DateTimeField(default=dt.datetime.utcnow)
    first_name = db.StringField(30)
    last_name = db.StringField(30)
    active = db.BooleanField(default=False)
    is_admin = db.BooleanField(default=False)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        super(User, self).__init__(username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)
