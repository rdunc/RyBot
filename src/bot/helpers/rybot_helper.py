#!/usr/bin/env python3

class RyBotHelper:
    def pluralize(number, phrase):
        if number > 1 or number == 0:
            return phrase + "s"
        else:
            return phrase
