#!/usr/bin/env python3

import json, time

from bot.lib.irc.irc import Irc
from bot.lib.core.log import Log
from bot.lib.commander import CommanderInit
from bot.helpers.rybot_helper import RyBotHelper

class CommanderCommands(CommanderInit):
    def load(self):
        command_path = self.command_path

        with open(command_path, "r") as of:
            commands = of.read()
            of.close()

        if len(commands) > 0:
            commands = json.loads(commands)
        else:
            commands = {}

        return commands

    def save(self, commands):
        command_path = self.command_path

        with open(command_path, "w") as of:
            json.dump(commands, of)
            of.close()

    def run(self, syntax):
        socket = self.socket
        channel = self.channel
        commands = self.load()
        command = commands[syntax]

        if self.exists(syntax):
            self.irc.send_message(socket, channel, command)
            return Log.commander("Running command {0}".format(syntax))

    def add(self, sender, syntax, response):
        socket = self.socket
        channel = self.channel
        interal_commands = ["!command", "!points"]

        if not syntax or not response or syntax in interal_commands:
            return self.irc.send_message(socket, channel, "@{0} -> Invalid syntax. Use !command new !<syntax> <response> instead.".format(sender))

        if not self.exists(syntax):
            command = ""

            for x in response:
                command += x + " "

            commands = self.load()
            commands[syntax] = command[:-2]

            self.save(commands)
            self.irc.send_message(socket, channel, "@{0} -> Command successfully created!".format(sender))
            return Log.commander("Command {0} successfully created!".format(syntax))
        else:
            return self.irc.send_message(socket, channel, "@{0} -> That command already exists. Use !command update !<syntax> <response> instead.".format(sender))

    def delete(self, sender, syntax):
        socket = self.socket
        channel = self.channel
        commands = self.load()

        if self.exists(syntax):
            commands.pop(syntax, None)
            self.save(commands)
            self.irc.send_message(socket, channel, "@{0} -> Command successfully deleted!".format(sender))
            return Log.commander("Command {0} successfully deleted!".format(syntax))

    def update(self, sender, syntax):
        if self.exists(syntax):
            commands = self.load()
            commands[syntax] = command[:-2]

            self.save(commands)
            self.irc.send_message(socket, channel, "@{0} -> Command successfully created!".format(sender))
            return Log.commander("Command {0} successfully created!".format(syntax))

    def exists(self, syntax):
        commands = self.load()

        if syntax in commands:
            return True
        else:
            return False
