#!/usr/bin/env python3

import requests, json, threading, sys
import collections, os, time

from bot.lib.economy import EconomyInit
from bot.lib.core.benchmark import Benchmark
from bot.lib.core.log import Log
from bot.helpers.color_helper import ColorHelper
from bot.helpers.rybot_helper import RyBotHelper
from collections import Counter

class Economy(EconomyInit):
    """Give all offline and online chatters points."""
    def give_points(self):
        config                  = self.config
        debug                   = config["debug"]
        point_timer             = config["give_points_timer"]
        api_chatters_url        = config["twitch_chatters_url"]
        economy_path            = "db/" + self.channel + "/economy.json"

        try:
            twitch_request = requests.get(api_chatters_url + self.channel + "/chatters")
            chatters_json = twitch_request.json()

            if debug:
                time_1 = Benchmark.start()

            with open(economy_path, "r") as of:
                file_chatters = of.read()
                of.close()

            if len(file_chatters) > 0:
                file_chatters = json.loads(file_chatters)

            if debug:
                Log.economy("Current file chatters count: {0}".format(len(file_chatters)))

            api_chatters = chatters_json["chatters"]["viewers"]
            chatters_dictionary = {}

            for i in api_chatters:
                chatters_dictionary[i] = 1

                if debug:
                    Log.economy("1 point was added to: {0}".format(i))

            if len(file_chatters) > 0:
                merged_chatters = [chatters_dictionary, file_chatters]
                merged_chatters = sum((Counter(dict(i)) for i in merged_chatters), Counter())
            else:
                merged_chatters = chatters_dictionary

            with open(economy_path, "w") as of:
                json.dump(merged_chatters, of)
                of.close()

            Log.economy("1 point was added to {0} {1}".format(len(merged_chatters), RyBotHelper.pluralize(len(merged_chatters), "chatter")))

            if debug:
                Log.economy("Current chatters from API: {0}".format(len(chatters_dictionary)))
                Benchmark.stop(time_1)
        except json.decoder.JSONDecodeError:
            Log.error("Problem decoding the JSON. Unable to distribute points.")
        except requests.exceptions.ConnectionError:
            Log.error("Unable to connect to the Twitch API.")
        except TypeError:
            Log.error("Error finding the viewers.")
        except FileNotFoundError:
            Log.error("Economy file not found. Unable to distribute points.")
