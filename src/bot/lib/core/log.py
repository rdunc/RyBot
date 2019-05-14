#!/usr/bin/env python3

from bot.helpers.color_helper import *

class Log:
    def debug(message):
        print("-> [{0}DEBUG{1}] {2}".format(ColorHelper.cyan(), ColorHelper.reset_all(), message))

    def info(message):
        print("-> [{0}INFO{1}] {2}".format(ColorHelper.magenta(), ColorHelper.reset_all(), message))

    def error(message):
        print("-> [{0}ERROR{1}] {2}".format(ColorHelper.red(), ColorHelper.reset_all(), message))

    def benchmark(message):
        print("-> [{0}BENCHMARK{1}] {2}".format(ColorHelper.cyan(), ColorHelper.reset_all(), message))

    def economy(message):
        print("-> [{0}ECONOMY{1}] {2}".format(ColorHelper.green(), ColorHelper.reset_all(), message))

    def announce(message):
        print("-> [{0}ANNOUNCER{1}] {2}".format(ColorHelper.green(), ColorHelper.reset_all(), message))

    def commander(message):
        print("-> [{0}COMMANDER{1}] {2}".format(ColorHelper.cyan(), ColorHelper.reset_all(), message))
