#!/usr/bin/env python3

import json, time

from bot.lib.irc.irc import Irc
from bot.lib.core.log import Log
from bot.lib.commander import CommanderInit
from bot.helpers.rybot_helper import RyBotHelper

class CommanderEconomy(CommanderInit):
    def check_points(self, sender):
        points = self.load()

        try:
            total_points = points[sender]
        except KeyError:
            total_points = 0

        Log.commander("Checking how many points {0} has.".format(sender))
        self.irc.send_message(self.socket, self.channel, "@{0} -> You have {1} {2}.".format(sender, total_points, RyBotHelper.pluralize(total_points, "point")))

    def load(self):
        economy_path = self.economy_path

        with open(economy_path, "r") as of:
            points = of.read()
            of.close()

        if len(points) > 0:
            points = json.loads(points)
        else:
            points = {}

        return points
