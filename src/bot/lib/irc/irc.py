#!/usr/bin/env python3

import sys

from bot.lib.core.log import Log
from bot.lib.irc import IrcInit

class Irc(IrcInit):
    """Connect to Twitch's IRC server using sockets"""
    def connect(self):
        config = self.config
        server = config["server"]
        port = config["port"]
        username = config["username"]
        password = config["oauth_password"]

        Log.info("Connecting to {0} on port {1}...".format(server, port))

        try:
            self.socket.settimeout(10)
            self.socket.connect((server, port))
            self.socket.settimeout(None)

            Log.info("Successfully connected to {0} on port {1}!".format(server, port))
            Log.info("Joining channel #{1}...".format(username, self.channel))

            self.socket.send(bytes("CAP REQ {0}\r\n".format(":twitch.tv/membership"), self.encoding_type))
            self.socket.send(bytes("PASS {0}\r\n".format(password), self.encoding_type))
            self.socket.send(bytes("NICK {0}\r\n".format(username), self.encoding_type))
            self.socket.send(bytes("JOIN #{0}\r\n".format(self.channel), self.encoding_type))

            Log.info("Successfully joined channel #{1}!".format(username, self.channel))

            return self.socket
        except:
            Log.error("Failed to connect to {0} on port {1}.".format(server, port))
            sys.exit(1)

    def send_ping(self, socket, message):
        socket.send(bytes("PING {0}\r\n".format(message), self.encoding_type))

    def send_pong(self, socket, message):
        socket.send(bytes("PONG {0}\r\n".format(message), self.encoding_type))

    def send_message(self, socket, channel, message):
        socket.send(bytes("PRIVMSG #{0} :{1}\r\n".format(channel, message), self.encoding_type))

    def leave_channel(self, socket, channel):
        socket.send(bytes("PART {0}\r\n".format(channel), self.encoding_type))
