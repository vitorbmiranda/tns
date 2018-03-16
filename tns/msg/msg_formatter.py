def wr_message(message):
    """
    :param message: Message instance with all the info
    :return: String with the formatted message
    """

    return "BREAKING! {0} just achieved {1} {2} {3}! Truly remarkable!".format(
        message.player_alias, message.level, message.difficulty, message.time
    )
