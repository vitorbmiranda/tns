# TODO: add multiple message templates
def wr_message(message):
    """
    :param message: Message instance with all the info
    :return: String with the formatted message
    """

    return "[the-elite.net] {0} just achieved {1} {2} {3}!".format(
        message.player_alias, message.level, message.difficulty, message.time
    )
