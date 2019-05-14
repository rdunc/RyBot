global config

config = {
    # Twitch Settings
    "server": "irc.twitch.tv",
    "port": 6667,
    "username": "",
    "oauth_password": "", # get this from https://twitchapps.com/tmi/
    "twitch_chatters_url": "https://tmi.twitch.tv/group/user/",

    # Bot Settings
    "enable_economy": False,
    "enable_announcer": False, # announces recently subscribed messages
    "enable_commander": False, # controls all channel commands

    # Economy Settings
    "give_points_timer": 15, # number of seconds

    # General Settings
    "debug": False,
    "encoding_type": "UTF-8",
    "socket_buffer_size": 2048
}
