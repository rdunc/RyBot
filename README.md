## What is RyBot?
This project is no longer maintained, and might not work right out of the box. It is recommended not to use this in production, this was just a test project.

RyBot is a simple Twitch IRC bot that I made in Python. RyBot comes equipped with an simple economy system to distribute points to all people that visited your channel. Feel free to build off this and let me know what you come up with. Please take into account that this bot is still in development, so you may run into bugs and or other unforseen issues while using this.

## Getting started
Before you can run RyBot you need to install its dependencies.

* ``` $ pip install requests ```
* ``` $ pip install colorama ```

After you've successfully installed the dependencies, you now need to configure the ```bot/config/config.py``` file.

* Open the ```bot/config/config.py```
* Replace ```username``` with the Twitch username that you want to use for your bot
* Replace ```oauth_password``` with your Twitch oauth password. Get yours [here](https://twitchapps.com/tmi/)
* Configure any of the other settings in the file to your liking

Now that you've configured the config.py file, we can now get the bot going!

* Open up a terminal, navigate to the RyBot root directory and type ```$ python run.py -c channel_name```. Replace channel_name with the name of the channel you wish the bot to enter.

Now that the bot's running you should start to see the chat inside your terminal window, this is an indication that it works.

## Commands
The commands are pretty basic right now. To run any of these commands you must type it into the channel the bot is currently in.

* ```!command new !<syntax> <response>``` - This will create a new command. Replace syntax with the name of your command (such as !welcome) and the response to whatever you want to be said in chat (such as Welcome to my channel! Don't forget to follow!). In this example when somebody types !welcome in chat, the bot will respond with 'Welcome to my channel! Don't forget to follow!'

* ```!<syntax>``` - Runs a command'
