#!/usr/bin/env python3

import os

from bot.lib.irc.irc import Irc
from bot.lib.economy.economy import Economy
from bot.lib.commander.commands import CommanderCommands
from bot.lib.commander.economy import CommanderEconomy
from bot.lib.announcer.announcer import Announcer

class RyBotInit(object):
    """
        Initialize all the things we need.

        Attributes:
            * channel: The Twitch channel to moderate in
            * config: The global config file variable
    """
    def __init__(self, channel, config):
        self.channel = channel
        self.config = config
        self.irc = Irc(channel, config)
        self.economy = Economy(channel, config)
        self.socket = self.irc.connect()
        self.commander_commands = CommanderCommands(self.socket, self.channel, self.config, self.irc)
        self.commander_economy = CommanderEconomy(self.socket, self.channel, self.config, self.irc)
        self.announcer = Announcer(self.irc, self.socket, self.config)

    """Creates all the files that we will use."""
    def create_files(self):
        db_path = "db/" + self.channel
        cache_path = db_path + "/cache.json"
        economy_path = db_path + "/economy.json"
        commands_path = db_path + "/commands.json"

        if not os.path.exists(db_path):
            os.makedirs(db_path)

        if not os.path.exists(cache_path):
            file = open(cache_path, "a")
            file.close()

        if not os.path.exists(economy_path):
            file = open(economy_path, "a")
            file.close()

        if not os.path.exists(commands_path):
            file = open(commands_path, "a")
            file.close()

    if __name__ == "__main__":
        self.create_files()
