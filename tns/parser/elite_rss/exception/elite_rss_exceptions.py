class EliteFeedParseInvalidHttpStatusException(Exception):
    """
    This is thrown when we try to access the-elite feed but we get a http status != 200
    """

    message = "Error accessing the-elite's URL ({0})! HTTP Status={1}"

    def __init__(self, url, status):
        super(EliteFeedParseInvalidHttpStatusException, self).__init__(self.message.format(url, status))

class EliteFeedParseNoLastIDException(Exception):
    """
    This is thrown when there is no last_id set in the meta_info table
    """

    message = "Not LAST_ID value in the META_INFO table!"

    def __init__(self, url, status):
        super(EliteFeedParseNoLastIDException, self).__init__(self.message.format(url, status))

