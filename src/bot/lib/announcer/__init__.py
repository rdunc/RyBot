#!/usr/bin/env python3

class AnnouncerInit:
    """
        Initialize all the things we need.

        Attributes:
            * config: The global config file variable
    """
    def __init__(self, irc, socket, config):
        self.irc = irc
        self.socket = socket
        self.config = config
