from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers
from zope.sqlalchemy import register
from sqlalchemy.orm import (scoped_session, sessionmaker, Session)
from .meta import Base

session_factory = sessionmaker(class_=Session)
DBSession = scoped_session(session_factory)
register(DBSession)

from .users import *
def includeme(config):
    """
    Initialize the model for a Pyramid app.

    Activate this setup using ``config.include('wiki.models')``.

    """
    settings = config.get_settings()
    engine = engine_from_config(
        settings, 'sqlalchemy.', client_encoding='utf8',
        max_identifier_length=30)  # , convert_unicode=True
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    #init_model()
