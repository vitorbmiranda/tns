class PRMessage():
    """
    This class represents one message that the notification job will pass to the 'messenger' module
    """

    def __init__(self, player_alias, game, level, difficulty, time, points):
        self.player_alias = player_alias
        self.game = game
        self.level = level
        self.difficulty = difficulty
        self.time = time
        self.points_given = points

    def __repr__(self):
        return ', '.join("%s: %s" % item for item in vars(self).items())
