# The variable WTF_CSRF_ENABLED determines if CSRF prevention should be enabled.
# The variable SECRET_KEY is a key used to create cryptographically secure tokens.
WTF_CSRF_ENABLED = True
SECRET_KEY = 'a-very-secret-secret-secret-that-is-very-secret'

import os
basedir = os.path.abspath(os.path.dirname(__file__))


# his configuration informs where SQLAlchemy will put the database file and
# where the migration data will be stored for upgrading the database when we
# make a change.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
