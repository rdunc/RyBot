#!/usr/bin/env python3

class EconomyInit(object):
    """
        Initialize all the things we need.

        Attributes:
            * channel: The Twitch channel to moderate in
            * config: The global config file variable
    """
    def __init__(self, channel, config):
        self.channel = channel
        self.config = config
