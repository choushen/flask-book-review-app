from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
collection = Table('collection', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=500)),
    Column('description', String(length=500)),
    Column('author', String(length=500)),
    Column('user_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=500)),
    Column('password', VARCHAR(length=500)),
    Column('email', VARCHAR(length=500)),
    Column('start_date', DATETIME),
    Column('collection_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['collection'].columns['user_id'].create()
    pre_meta.tables['user'].columns['collection_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['collection'].columns['user_id'].drop()
    pre_meta.tables['user'].columns['collection_id'].create()
