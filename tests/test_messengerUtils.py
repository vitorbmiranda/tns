from unittest import TestCase
from tns.msg.utils import MessengerUtils


class TestMessengerUtils(TestCase):

    def test_mask_phone_number(self):
        utils = MessengerUtils()
        self.assertEqual('4567', utils.mask_phone_number("+55111234567"))

