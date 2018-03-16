class FeedItem():
    """
    This class represents one feed item from the-elite's RSS feed so it' easier to access info
    """

    def __init__(self, title, link, description, pub_date):
        self.title = title
        self.link = link
        self.description = description
        self.pub_date = pub_date

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
