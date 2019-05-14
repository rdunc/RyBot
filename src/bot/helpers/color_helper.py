#!/usr/bin/env python3

from colorama import init, Fore, Back, Style

class ColorHelper:
    """Initialize all the things we need."""
    def __init__(self, config):
        init()


    def reset_all():
        return Fore.RESET + Style.RESET_ALL


    def red():
        return Fore.RED + Style.BRIGHT


    def green():
        return Fore.GREEN + Style.BRIGHT


    def cyan():
        return Fore.CYAN + Style.BRIGHT


    def white():
        return Fore.WHITE + Style.BRIGHT


    def magenta():
        return Fore.MAGENTA + Style.BRIGHT
