#!/usr/bin/env python3

class CommanderInit(object):
    def __init__(self, socket, channel, config, irc):
        self.channel = channel
        self.config = config
        self.socket = socket
        self.irc = irc
        self.economy_path = "db/" + self.channel + "/economy.json"
        self.command_path = "db/" + self.channel + "/commands.json"
