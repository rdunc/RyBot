#!/usr/bin/env python3

from bot.lib.commander.commands import CommanderCommands
from bot.lib.commander.economy import CommanderEconomy

class IrcHelper:
    def get_sender(message):
        result = ""

        for char in message:
            if char == "!":
                break
            if char != ":":
                result += char

        return result

    def get_message(message):
        result = ""
        i = 3
        length = len(message)

        while i < length:
            result += message[i] + " "
            i += 1

        return result[1::]

    def parse_message(commander_commands, commander_economy, sender, message):
        message = message.split(" ")
        syntax = message[0]

        if commander_commands.exists(syntax):
            return commander_commands.run(syntax)
        else:
            command = message[1]

            if not command:
                if syntax == "!points":
                    return commander_economy.check_points(sender)
            else:
                user_command_syntax = message[2]

                if syntax == "!command":
                    if command == "new":
                        user_command_response = message[3:]
                        return commander_commands.add(sender, user_command_syntax, user_command_response)
                    if command == "delete":
                        command_to_delete = message[2]
                        return commander_commands.delete(sender, command_to_delete)
