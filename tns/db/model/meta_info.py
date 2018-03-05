from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from tns.db.database import Base


class MetaInfo(Base):

    __tablename__ = 'meta_info'

    id = Column(Integer, primary_key=True)
    key = Column(String(256), nullable=False)
    value = Column(String(1024), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updatd_at = Column(DateTime, default=datetime.now)

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
