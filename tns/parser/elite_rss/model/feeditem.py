class FeedItem():
    """
    This class represents one feed item from the-elite's RSS feed so it' easier to access info
    """

    def __init__(self, title, link, description, pub_date, game, is_wr, is_untied_wr, player_name, player_alias,
                 stage, difficulty, time_hms, video_type, video_id):
        self.title = title
        self.link = link
        self.description = description
        self.pub_date = pub_date
        self.game = game
        self.is_wr = is_wr
        self.is_untied_wr = is_untied_wr
        self.player_name = player_name
        self.player_alias = player_alias
        self.stage = stage
        self.difficulty = difficulty
        self.time_hms = time_hms
        self.video_type = video_type
        self.video_id = video_id

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
