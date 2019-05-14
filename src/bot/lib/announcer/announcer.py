#!/usr/bin/env python3

from bot.lib.announcer import AnnouncerInit
from bot.lib.core.log import Log

class Announcer(AnnouncerInit):
    def announce_subscription(self, message):
        if self.config["enable_announcer"]:
            message_split = message.split()

            self.irc.send_message(
                self.socket,
                self.channel,
                "Thank you {0} for subscribing!".format(message_split[0])
            )

        Log.announce(message)
