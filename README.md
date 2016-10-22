# Fantascraper
General scripts for fantasy EPL

fantascraper.py mostly works, needs more testing.

physioroom.py works, probably needs more testing.

### Prereqs

1. python
2. pip
3. virtualenv (optional, but suggested)

Use pip to install required pip packages
```
$ pip install -r requirements.txt
```

### Configuration

```
$ git clone https://github.com/soehlert/fantascraper.git
```

Edit fantascraper.conf by entering the proper things.

To find your league id and team id go to your roster page in fantrax. In the url bar you'll see `teamID=xxxxx&` where the xxxxxx (NOT INCLUDING THE &) is a random string that is your team id. The league id will look like `leagueID=xxxxxxx&` and same thing there.

Replace team.csv with a file full of your players (One player per line, first initial and last name):

```
H Kane
E Dier
```

Or even better, now run fantascraper.py and let it create the team.csv file for you.

Edit the physioroom.conf file by entering a channel id and a token.

To get the channel id (works with public, private or DMs), go to [groups.list page](https://api.slack.com/methods/groups.list/test) if you want to use a private room, [IMs list page](https://api.slack.com/methods/im.list/test) if you want to use a DM though you'll have to figure out user id numbers, or [channels list page](https://api.slack.com/methods/channels.list/test) to use a public room. Once on the page, click `Test method` and then search for the room you want.

To get a token, go to [this page](https://api.slack.com/web) and click `Generate test tokens` This is a little dirty to use test tokens like this, but I don't wanna figure out how to make it an app just yet.

### Usage

```
usage: fantascraper.py [-h] [--version] [-c CONF_FILE] [-t TEAM_FILE]

optional arguments:
  -h, --help                        show this help message and exit
  --version                         Print version
  -c CONF_FILE, --config CONF_FILE  Specify config file location
  -t TEAM_FILE, --team TEAM_FILE    Specify team file location
```

```
usage: physioroom.py [-h] [--version] [-c CONF_FILE] [-t TEAM_FILE]

optional arguments:
  -h, --help                        show this help message and exit
  --version                         Print version
  -c CONF_FILE, --config CONF_FILE  Specify config file location
  -t TEAM_FILE, --team TEAM_FILE    Specify team file location
```

That should get you able to run the script once through no problem. If you'd like to set it to run on a schedule (once a day? once a week before the games start?), you'll need to use cron or something similar. (No promises any of this works on Windows).

##TODO

1. Allow bulk import (ie whole team at once) √
2. OOP √ish
3. Automate filling out team list √
4. Add script to check starting lineups via twitter
5. Turn into an app so we can use oauth instead of test tokens
6. Switch to using http://www.rotoworld.com/teams/injuries/bpl/all/
