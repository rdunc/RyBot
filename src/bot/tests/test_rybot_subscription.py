#!/usr/bin/env python3

"""Subsciption Tests"""

import unittest

class RybotSubscriptionTest(unittest.TestCase):
    def test_twitch_notify(self):
        message = "SomeRandomUsername subscribed for 6 months in a row!"
        message_split = message.split()

        self.assertEqual(message_split[0], "SomeRandomUsername")


if __name__ == "__main__":
    unittest.main()
