import sys
import logging.config
import tns.crypto.tns_crypto as tns_crypto
import tns.db.database as tns_database
import tns.tns_startup as tns_startup
from tns.db.model.player import Player

logger = logging.getLogger(__name__)

tns_startup.main(False)
session = tns_database.Session()

if len(sys.argv) != 4:
    raise Exception('Usage: python insert_player.py <rankings_id> <name> <telnumber>')

# get data from argv
p_rankings_id = sys.argv[1]
p_name = sys.argv[2]
p_telnumber = sys.argv[3]

player = Player(p_rankings_id, p_name, tns_crypto.encrypt(p_telnumber))

session.add(player)
session.commit()
session.close()
