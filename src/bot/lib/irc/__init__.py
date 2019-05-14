#!/usr/bin/env python3

import socket

class IrcInit(object):
    """
        Initialize all the things we need.

        Attributes:
            * channel: The Twitch channel to moderate in
            * config: The global config file variable
    """
    def __init__(self, channel, config):
        self.channel = channel
        self.config = config
        self.socket = socket.socket()
        self.encoding_type = config["encoding_type"]
