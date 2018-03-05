from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from tns.db.database import Base
from tns.db.model.player_subscription import PlayerSubscription


class Player(Base):

    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    rankings_id = Column(Integer, nullable=False, unique=True)
    alias = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updatd_at = Column(DateTime, default=datetime.now)

    def __init__(self, rankings_id, alias, phone_number):
        self.rankings_id = rankings_id
        self.alias = alias
        self.phone_number = phone_number

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())

Player.subscriptions = relationship(
    'PlayerSubscription',
    order_by=PlayerSubscription.subscription_type_id,
    back_populates='player')
