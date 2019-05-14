#!/usr/bin/env python3

from bot.lib.cache import CacheInit

class Cache(CacheInit):
    def load(self):
        with open(self.cache_path, "r") as of:
            cache = of.read()
            of.close()

        if cache:
            cache = json.loads(cache)
        else:
            cache = {}

        return cache

    def save(self, cache):
        with open(self.cache_path, "w") as of:
            json.dump(cache, of)
            of.close()

    def get(self, key):
        pass

    def put(self):
        pass

    def update(self):
        pass
