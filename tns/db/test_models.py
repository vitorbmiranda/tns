import tns.db.database as tns_database
from tns.db.model.player import Player
from tns.db.model.subscription_type import SubscriptionType
from tns.db.model.player_subscription import PlayerSubscription
from tns.db.model.meta_info import MetaInfo
import tns.crypto.tns_crypto as tns_crypto


def do_test():
    session = tns_database.Session()

    player_one = Player('00001', 'Player One', tns_crypto.encrypt('9999999999'))
    player_two = Player('00002', 'Player Two', tns_crypto.encrypt('1010101010'))

    session.add(player_one)
    session.add(player_two)
    session.flush()
    session.refresh(player_one)
    session.refresh(player_two)

    sub_type_wrs= SubscriptionType('SUB_WRS', 'World Records / Untied World Records')
    sub_type_bops = SubscriptionType('SUB_BOPS', 'Player Bops')

    session.add(sub_type_wrs)
    session.add(sub_type_bops)
    session.flush()
    session.refresh(sub_type_wrs)
    session.refresh(sub_type_bops)

    player_one_sub_wrs = PlayerSubscription(player_one, sub_type_wrs)
    player_one_sub_bops = PlayerSubscription(player_one, sub_type_bops)

    player_two_sub_wrs = PlayerSubscription(player_two, sub_type_wrs)

    session.add(player_one_sub_wrs)
    session.add(player_one_sub_bops)
    session.add(player_two_sub_wrs)

    meta_info_last_pr = MetaInfo("LAST_PR_FETCHED", "1234")
    session.add(meta_info_last_pr)

    session.commit()

    session.close()

