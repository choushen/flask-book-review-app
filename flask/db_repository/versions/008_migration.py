from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
landlord = Table('landlord', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=500)),
    Column('contact_number', VARCHAR(length=20)),
    Column('address', VARCHAR(length=500)),
)

property = Table('property', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('address', VARCHAR(length=500)),
    Column('start_date', DATETIME),
    Column('duration', INTEGER),
    Column('rent', FLOAT),
    Column('landlord_id', INTEGER),
)

collection = Table('collection', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=500)),
    Column('description', String(length=500)),
    Column('author', String(length=500)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=500)),
    Column('password', String(length=500)),
    Column('email', String(length=500)),
    Column('start_date', DateTime),
    Column('collection_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['landlord'].drop()
    pre_meta.tables['property'].drop()
    post_meta.tables['collection'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['landlord'].create()
    pre_meta.tables['property'].create()
    post_meta.tables['collection'].drop()
    post_meta.tables['user'].drop()
