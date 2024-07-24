from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
userDB = Table('userDB', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=25)),
    Column('password', String(length=25)),
    Column('email', String(length=50)),
    Column('create_date', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['userDB'].columns['email'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['userDB'].columns['email'].drop()
