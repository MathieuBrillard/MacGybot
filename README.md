# "MacGybot"
## _a discord bot in python_

MacGybot is a discord bot, working with lightbulb and hikari.py.

## Features

- Create events (every event is saved in a .sqlite file until it is due.)
- Generate calendars according to the events registered in the database.
- List events registered at a given date.
- Create polls.

## Installation

First of all, you need to download [python] (I used v3.9.7 to write this bot).

Now, start a terminal inside the bot folder.
You can download automatically the libraries used in the bot by tipping this command :
```sh
# python librairies
python install/install.py
# generate the sqlite database
cd assets/db/
python gen_db.py
# go back at the bot root folder
cd ../.. 
```

To launch the bot, just need to run the following : 
```sh
python bot.py
```

## Development

You can get the lastest version of the bot on the following [repository].

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [repository]: <https://github.com/MathieuBrillard/MacGybot/>
   [python]: <https://www.python.org/downloads/>
   [ffmpeg]: <https://www.gyan.dev/ffmpeg/builds/>
