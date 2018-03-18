class MessengerUtils:

    # TODO use a better method for hiding the player's # (e.g: +55****0101)
    # noinspection PyMethodMayBeStatic
    def mask_phone_number(self, phone_number):
        """

        :param phone_number: a phone number
        :return: masked number
        """
        return phone_number[-4:]