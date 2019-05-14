#!/usr/bin/env python3

import re, threading, time

from bot import RyBotInit
from bot.lib.core.log import Log
from bot.helpers.irc_helper import IrcHelper
from bot.helpers.color_helper import ColorHelper

class RyBot(RyBotInit):
    """Run the RyBot. Let's get this thing rollin!"""
    def run(self):
        config = self.config

        if self.socket:
            threading.Thread(target=self.start_pong).start()

            if config["enable_economy"]:
                threading.Thread(target=self.start_economy).start()

            while True:
                self.parse_data()

    """Parse the data from the socket"""
    def parse_data(self):
        data = ""
        config = self.config
        encoding_type = config["encoding_type"]
        buffer_size = config["socket_buffer_size"]
        debug = config["debug"]

        try:
            data = data + self.socket.recv(buffer_size).decode("ascii")
        except UnicodeDecodeError:
            Log.error("Message cannot be decoded.")

        data_split = re.split(r"[~\r\n]+", data)
        data = data_split.pop()

        for line in data_split:
            line = str.rstrip(line)
            line = str.split(line)

            try:
                if line[0] == "PING":
                    self.irc.send_pong(self.socket, line[1])

                    if debug:
                        Log.debug("Pong sent.")

                if line[1] == "PRIVMSG":
                    sender = IrcHelper.get_sender(line[0])
                    message = IrcHelper.get_message(line)

                    print("-> [{0}{1}{2}]: {3}".format(ColorHelper.white(), sender, ColorHelper.reset_all(), message))

                    if sender == "twitchnotify":
                        self.announcer.announce_subscription(message)

                    if config["enable_commander"]:
                        IrcHelper.parse_message(self.commander_commands, self.commander_economy, sender, message)
            except IndexError:
                if debug:
                    print(data)
                    Log.error("Index out of range error occured.")

    def start_economy(self):
        config = self.config
        points_timer = config["give_points_timer"]
        debug = config["debug"]

        Log.economy("Giving points.")

        self.economy.give_points()
        threading.Timer(points_timer, self.start_economy).start()

    def start_pong(self):
        config = self.config
        socket = self.socket
        debug = config["debug"]

        self.irc.send_pong(self.socket, ":tmi.twitch.tv")
        threading.Timer(58, self.start_pong).start()

        if debug:
            Log.debug("Pong sent.")
