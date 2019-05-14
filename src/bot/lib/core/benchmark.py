#!/usr/bin/env python3

import time

from bot.lib.core.log import Log

class Benchmark:
    def start():
        Log.benchmark("Started.")
        return time.time()

    def stop(time_1):
        time_2 = time.time()
        Log.benchmark("Finished. Function took {0} seconds to complete.".format(time_2 - time_1))
