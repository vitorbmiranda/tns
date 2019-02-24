import tns.db.database as database
from tns.db.model.meta_info import MetaInfo

LAST_ID_KEY = "LAST_ID"


def update_last_id_meta_info(session, last_id):
    """
    Add the last RSS feed item id (which is the-elite record ID) to the meta_info table.
    :param session: db session
    :param last_id: ID of the RSS feed item saved
    """
    meta = session.query(MetaInfo). \
        filter(MetaInfo.key == LAST_ID_KEY). \
        one()
    meta.value = last_id


def get_last_id_meta_info():
    """
    Retrieve the last RSS feed item id from the meta_info table.
    :param session: db session
    :return: ID of the last RSS feed item
    """
    session = database.Session()
    meta = session.query(MetaInfo). \
        filter(MetaInfo.key == LAST_ID_KEY). \
        one()
    session.close()
    return meta
