from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from tns.db.database import Base
from tns.db.model.player_subscription import PlayerSubscription
import tns.crypto.tns_crypto as tns_crypto

class Player(Base):

    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    rankings_id = Column(Integer, nullable=False, unique=True)
    alias = Column(String(64), nullable=False)
    phone_number = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, rankings_id, alias, phone_number):
        self.rankings_id = rankings_id
        self.alias = alias
        self.phone_number = phone_number

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())

    # TODO: maybe change to hybrid properties? https://docs.sqlalchemy.org/en/latest/orm/mapped_attributes.html
    @property
    def decrypted_phone_number(self):
        return tns_crypto.decrypt(self.phone_number)


Player.subscriptions = relationship(
    'PlayerSubscription',
    order_by=PlayerSubscription.subscription_type_id,
    back_populates='player')
