from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import logging.config

logger = logging.getLogger(__name__)

Session = None
Engine = None
Base = declarative_base()


def init(db_url):
    """
    Initialize SQL Alchemy base structure

    :param db_url: DB Connection URL string
    """

    global Session
    global Engine
    global Base

    engine = create_engine(db_url)

    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()

    Session = sessionmaker(bind=engine)
    Engine = engine


def create():
    """Recreate the DB schema"""
    Base.metadata.drop_all(bind=Engine)
    Base.metadata.create_all(bind=Engine)
