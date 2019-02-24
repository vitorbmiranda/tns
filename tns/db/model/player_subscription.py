from datetime import datetime
from sqlalchemy import ForeignKey, Column, Integer, DateTime
from sqlalchemy.orm import relationship

from tns.db.database import Base


class PlayerSubscription(Base):

    __tablename__ = 'player_subscription'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player.id"), nullable=False)
    player = relationship('Player', back_populates='subscriptions')

    subscription_type_id = Column(Integer, ForeignKey("subscription_type.id"), nullable=False)
    subscription_type = relationship('SubscriptionType')

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, player, subscription_type):
        self.player_id = player.id
        self.subscription_type_id = subscription_type.id

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
