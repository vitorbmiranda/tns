from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from tns.db.database import Base


class SubscriptionType(Base):

    __tablename__ = 'subscription_type'

    id = Column(Integer, primary_key=True)
    key = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, key, name):
        self.key = key
        self.name = name

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
