#!/usr/bin/env python3

import sys, getopt, os

from bot.rybot import RyBot
from bot.config.config import *
from bot.lib.core.log import Log

def run(argv):
    try:
        opts, args = getopt.getopt(argv, "hc:", ["channel="])

        if not opts:
            Log.error("You forgot to enter a channel.")
            Log.info("Usage: run.py -c <channel>\n")
            sys.exit(1)
        else:
            for opt, arg in opts:
                if opt == "-help":
                    print("\nUsage: run.py -c <channel>")
                    sys.exit(1)

                if opt in ("-c", "--channel"):
                    channel = arg

            if os.path.exists("bot/config/config.py"):
                if config["username"]:
                    if config["oauth_password"]:
                        RyBot(channel, config).run()
                    else:
                        Log.error("Password was invalid. Please make sure you configured the config.py file correctly.")
                else:
                    Log.error("Username was invalid. Please make sure you configured the config.py file correctly.")
            else:
                Log.error("No config file was found. Please make sure you configured the config.py file correctly.")
    except getopt.GetoptError:
        print("\nUsage: run.py -c <channel>")
        sys.exit(1)

if __name__ == "__main__":
    run(sys.argv[1:])
